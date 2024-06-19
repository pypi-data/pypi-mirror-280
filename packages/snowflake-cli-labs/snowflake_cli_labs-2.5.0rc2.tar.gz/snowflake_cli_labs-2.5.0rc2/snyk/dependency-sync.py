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

from pathlib import Path

import tomlkit


def sync():
    pyproject = tomlkit.loads(Path("pyproject.toml").read_text())
    dependencies = pyproject["project"]["dependencies"]
    dev_dependencies = pyproject["project"]["optional-dependencies"]["development"]
    with open("snyk/requirements.txt", "w") as req:
        for dep in dependencies:
            req.write(f"{dep}\n")
        for dep in dev_dependencies:
            req.write(f"{dep}\n")


if __name__ == "__main__":
    sync()
