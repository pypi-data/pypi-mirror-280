# Copyright (c) 2024 Snowflake Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import re
from typing import Dict, List, Optional, Set

from snowflake.cli.api.constants import ObjectType
from snowflake.cli.api.identifiers import FQN
from snowflake.cli.api.project.schemas.snowpark.argument import Argument
from snowflake.cli.api.sql_execution import SqlExecutionMixin
from snowflake.cli.plugins.snowpark.models import Requirement
from snowflake.cli.plugins.snowpark.package_utils import (
    generate_deploy_stage_name,
)
from snowflake.connector.cursor import SnowflakeCursor

DEFAULT_RUNTIME = "3.8"


def check_if_replace_is_required(
    object_type: ObjectType,
    current_state,
    handler: str,
    return_type: str,
    snowflake_dependencies: List[str],
    external_access_integrations: List[str],
    imports: List[str],
    stage_artifact_file: str,
) -> bool:
    import logging

    log = logging.getLogger(__name__)
    resource_json = _convert_resource_details_to_dict(current_state)
    old_dependencies = resource_json["packages"]
    log.info(
        "Found %d defined Anaconda packages in deployed %s...",
        len(old_dependencies),
        object_type,
    )
    log.info("Checking if app configuration has changed...")

    if _snowflake_dependencies_differ(old_dependencies, snowflake_dependencies):
        log.info(
            "Found difference of package requirements. Replacing the %s.", object_type
        )
        return True

    if set(external_access_integrations) != set(
        resource_json.get("external_access_integrations", [])
    ):
        log.info(
            "Found difference of external access integrations. Replacing the %s.",
            object_type,
        )
        return True

    if (
        resource_json["handler"].lower() != handler.lower()
        or _sql_to_python_return_type_mapper(resource_json["returns"]).lower()
        != return_type.lower()
    ):
        log.info(
            "Return type or handler types do not match. Replacing the %s.", object_type
        )
        return True

    if _compare_imports(resource_json, imports, stage_artifact_file):
        return True

    return False


def _convert_resource_details_to_dict(function_details: SnowflakeCursor) -> dict:
    import json

    function_dict = {}
    json_properties = ["packages", "installed_packages"]
    for function in function_details:
        if function[0] in json_properties:
            function_dict[function[0]] = json.loads(
                function[1].replace("'", '"'),
            )
        else:
            function_dict[function[0]] = function[1]
    return function_dict


def _snowflake_dependencies_differ(
    old_dependencies: List[str], new_dependencies: List[str]
) -> bool:
    def _standardize(packages: List[str]) -> Set[str]:
        return set(
            Requirement.parse_line(package).name_and_version for package in packages
        )

    return _standardize(old_dependencies) != _standardize(new_dependencies)


def _sql_to_python_return_type_mapper(resource_return_type: str) -> str:
    """
    Some of the Python data types get converted to SQL types, when function/procedure is created.
    So, to properly compare types, we use mapping based on:
    https://docs.snowflake.com/en/developer-guide/udf-stored-procedure-data-type-mapping#sql-python-data-type-mappings

    Mind you, this only applies to cases, in which Snowflake accepts Python type as return.
    Ie. if function returns list, it has to be declared as 'array' during creation,
    therefore any conversion is not necessary
    """
    mapping = {
        "number(38,0)": "int",
        "timestamp_ntz(9)": "datetime",
        "timestamp_tz(9)": "datetime",
        "varchar(16777216)": "string",
    }

    return mapping.get(resource_return_type.lower(), resource_return_type.lower())


class SnowparkObjectManager(SqlExecutionMixin):
    @property
    def _object_type(self) -> ObjectType:
        raise NotImplementedError()

    @property
    def _object_execute(self):
        raise NotImplementedError()

    def create(self, *args, **kwargs) -> SnowflakeCursor:
        raise NotImplementedError()

    def execute(self, execution_identifier: str) -> SnowflakeCursor:
        return self._execute_query(f"{self._object_execute} {execution_identifier}")

    @staticmethod
    def artifact_stage_path(identifier: str):
        return generate_deploy_stage_name(identifier).lower()

    def create_query(
        self,
        identifier: str,
        return_type: str,
        handler: str,
        artifact_file: str,
        packages: List[str],
        imports: List[str],
        external_access_integrations: Optional[List[str]] = None,
        secrets: Optional[Dict[str, str]] = None,
        runtime: Optional[str] = None,
        execute_as_caller: bool = False,
    ) -> str:
        imports.append(artifact_file)
        imports = [f"'{x}'" for x in imports]
        packages_list = ",".join(f"'{p}'" for p in packages)

        query = [
            f"create or replace {self._object_type.value.sf_name} {identifier}",
            f"copy grants",
            f"returns {return_type}",
            "language python",
            f"runtime_version={runtime or DEFAULT_RUNTIME}",
            f"imports=({', '.join(imports)})",
            f"handler='{handler}'",
            f"packages=({packages_list})",
        ]

        if external_access_integrations:
            external_access_integration_name = ",".join(
                f"{e}" for e in external_access_integrations
            )
            query.append(
                f"external_access_integrations=({external_access_integration_name})"
            )

        if secrets:
            secret_name = ",".join(f"'{k}'={v}" for k, v in secrets.items())
            query.append(f"secrets=({secret_name})")

        if execute_as_caller:
            query.append("execute as caller")

        return "\n".join(query)


def _is_signature_type_a_string(sig_type: str) -> bool:
    return sig_type.lower() in ["string", "varchar"]


def build_udf_sproc_identifier(
    udf_sproc,
    slq_exec_mixin,
    include_parameter_names,
    include_default_values=False,
):
    def format_arg(arg: Argument):
        result = f"{arg.arg_type}"
        if include_parameter_names:
            result = f"{arg.name} {result}"
        if include_default_values and arg.default:
            val = f"{arg.default}"
            if _is_signature_type_a_string(arg.arg_type):
                val = f"'{val}'"
            result += f" default {val}"
        return result

    if udf_sproc.signature and udf_sproc.signature != "null":
        arguments = ", ".join(format_arg(arg) for arg in udf_sproc.signature)
    else:
        arguments = ""

    name = FQN.from_identifier_model(udf_sproc).using_context().identifier
    return f"{name}({arguments})"


def _compare_imports(
    resource_json: dict, imports: List[str], artifact_file: str
) -> bool:
    pattern = re.compile(r"(?:\[@?\w+_\w+\.)?(\w+(?:/\w+)+\.\w+)(?:\])?")

    project_imports = {
        imp
        for import_string in [*imports, artifact_file]
        for imp in pattern.findall(import_string.lower())
    }

    if "imports" not in resource_json.keys():
        object_imports = set()
    else:
        object_imports = {
            imp.lower()
            for imp in pattern.findall(resource_json.get("imports", "").lower())
        }

    return project_imports != object_imports
