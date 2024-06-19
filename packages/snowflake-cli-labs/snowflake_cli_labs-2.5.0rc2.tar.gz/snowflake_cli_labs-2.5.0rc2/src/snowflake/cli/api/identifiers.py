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

from click import ClickException
from snowflake.cli.api.cli_global_context import cli_context
from snowflake.cli.api.exceptions import FQNInconsistencyError, FQNNameError
from snowflake.cli.api.project.schemas.identifier_model import ObjectIdentifierBaseModel
from snowflake.cli.api.project.util import VALID_IDENTIFIER_REGEX, identifier_for_url


class FQN:
    """
    Class representing an identifier and supporting fully qualified names.

    The instance supports builder pattern that allows updating the identifier with database and
    schema from different sources. For example:

    fqn = FQN.from_string("my_schema.object").using_connection(conn)
    fqn = FQN.from_identifier_model(cli_context.project_definition.streamlit).using_context()
    fqn = FQN.from_string("my_name").set_database("db").set_schema("foo")
    """

    def __init__(self, database: str | None, schema: str | None, name: str):
        self._database = database
        self._schema = schema
        self._name = name

    @property
    def database(self) -> str | None:
        return self._database

    @property
    def schema(self) -> str | None:
        return self._schema

    @property
    def name(self) -> str:
        return self._name

    @property
    def identifier(self) -> str:
        if self.database:
            return f"{self.database}.{self.schema if self.schema else 'PUBLIC'}.{self.name}"
        if self.schema:
            return f"{self.schema}.{self.name}"
        return self.name

    @property
    def url_identifier(self) -> str:
        return ".".join(identifier_for_url(part) for part in self.identifier.split("."))

    def __str__(self):
        return self.identifier

    def __eq__(self, other):
        return self.identifier == other.identifier

    @classmethod
    def from_string(cls, identifier: str) -> "FQN":
        """
        Takes in an object name in the form [[database.]schema.]name. Returns a FQN instance.
        """
        qualifier_pattern = rf"(?:(?P<first_qualifier>{VALID_IDENTIFIER_REGEX})\.)?(?:(?P<second_qualifier>{VALID_IDENTIFIER_REGEX})\.)?(?P<name>{VALID_IDENTIFIER_REGEX})(?P<signature>\(.*\))?"
        result = re.fullmatch(qualifier_pattern, identifier)

        if result is None:
            raise FQNNameError(identifier)

        unqualified_name = result.group("name")
        if result.group("second_qualifier") is not None:
            database = result.group("first_qualifier")
            schema = result.group("second_qualifier")
        else:
            database = None
            schema = result.group("first_qualifier")
        if signature := result.group("signature"):
            unqualified_name = unqualified_name + signature
        return cls(name=unqualified_name, schema=schema, database=database)

    @classmethod
    def from_identifier_model(cls, model: ObjectIdentifierBaseModel) -> "FQN":
        """Create an instance from object model."""
        if not isinstance(model, ObjectIdentifierBaseModel):
            raise ClickException(
                f"Expected {type(ObjectIdentifierBaseModel)}, got {model}."
            )

        fqn = cls.from_string(model.name)

        if fqn.database and model.database:
            raise FQNInconsistencyError("database", model.name)
        if fqn.schema and model.schema_name:
            raise FQNInconsistencyError("schema", model.name)

        return fqn.set_database(model.database).set_schema(model.schema_name)

    def set_database(self, database: str | None) -> "FQN":
        if database:
            self._database = database
        return self

    def set_schema(self, schema: str | None) -> "FQN":
        if schema:
            self._schema = schema
        return self

    def set_name(self, name: str) -> "FQN":
        self._name = name
        return self

    def using_connection(self, conn) -> "FQN":
        """Update the instance with database and schema from connection."""
        # Update the identifier only it if wasn't already a qualified name
        if conn.database and not self.database:
            self.set_database(conn.database)
        if conn.schema and not self.schema:
            self.set_schema(conn.schema)
        return self

    def using_context(self) -> "FQN":
        """Update the instance with database and schema from connection in current cli context."""
        return self.using_connection(cli_context.connection)
