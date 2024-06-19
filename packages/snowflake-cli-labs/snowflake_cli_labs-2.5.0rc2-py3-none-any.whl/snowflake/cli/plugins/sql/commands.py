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

from pathlib import Path
from typing import List, Optional

import typer
from snowflake.cli.api.commands.flags import (
    parse_key_value_variables,
    project_definition_option,
)
from snowflake.cli.api.commands.snow_typer import SnowTyperFactory
from snowflake.cli.api.output.types import CommandResult, MultipleResults, QueryResult
from snowflake.cli.plugins.sql.manager import SqlManager

# simple Typer with defaults because it won't become a command group as it contains only one command
app = SnowTyperFactory()


def _parse_key_value(key_value_str: str):
    parts = key_value_str.split("=")
    if len(parts) < 2:
        raise ValueError("Passed key-value pair does not comform with key=value format")

    return parts[0], "=".join(parts[1:])


@app.command(name="sql", requires_connection=True, no_args_is_help=True)
def execute_sql(
    query: Optional[str] = typer.Option(
        None,
        "--query",
        "-q",
        help="Query to execute.",
    ),
    files: Optional[List[Path]] = typer.Option(
        None,
        "--filename",
        "-f",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        help="File to execute.",
    ),
    std_in: Optional[bool] = typer.Option(
        False,
        "--stdin",
        "-i",
        help="Read the query from standard input. Use it when piping input to this command.",
    ),
    data_override: List[str] = typer.Option(
        None,
        "--variable",
        "-D",
        help="String in format of key=value. If provided the SQL content will "
        "be treated as template and rendered using provided data.",
    ),
    _: Optional[str] = project_definition_option(optional=True),
    **options,
) -> CommandResult:
    """
    Executes Snowflake query.

    Use either query, filename or input option.

    Query to execute can be specified using query option, filename option (all queries from file will be executed)
    or via stdin by piping output from other command. For example `cat my.sql | snow sql -i`.

    The command supports variable substitution that happens on client-side. Both &VARIABLE or &{ VARIABLE }
    syntax are supported.
    """
    data = {}
    if data_override:
        data = {v.key: v.value for v in parse_key_value_variables(data_override)}

    single_statement, cursors = SqlManager().execute(query, files, std_in, data=data)
    if single_statement:
        return QueryResult(next(cursors))
    return MultipleResults((QueryResult(c) for c in cursors))
