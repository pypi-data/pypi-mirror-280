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

from snowflake.cli.api.plugins.command import (
    CommandPath,
    CommandSpec,
    CommandType,
    plugin_hook_impl,
)
from snowflakecli.test_plugins.override_build_in_command import commands


@plugin_hook_impl
def command_spec():
    return CommandSpec(
        parent_command_path=CommandPath(["connection"]),
        command_type=CommandType.SINGLE_COMMAND,
        typer_instance=commands.app,
    )
