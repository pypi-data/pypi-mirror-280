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

import os
import shutil
import subprocess
import tempfile
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from snowflake.cli import __about__

TEST_DIR = Path(__file__).parent


@pytest.fixture(scope="session")
def test_root_path():
    return TEST_DIR


@pytest.fixture(autouse=True)
def disable_colors_and_styles_in_output(monkeypatch):
    """
    Colors and styles in output cause mismatches in asserts,
    this environment variable turn off styling
    """
    monkeypatch.setenv("TERM", "unknown")


@pytest.fixture
def temp_dir():
    initial_dir = os.getcwd()
    tmp = tempfile.TemporaryDirectory()
    os.chdir(tmp.name)
    yield tmp.name
    os.chdir(initial_dir)
    tmp.cleanup()


@pytest.fixture(scope="session")
def snowcli(test_root_path):
    with TemporaryDirectory() as tmp_dir:
        tmp_dir_path = Path(tmp_dir)
        _create_venv(tmp_dir_path)
        _build_snowcli(tmp_dir_path, test_root_path)
        _install_snowcli_with_external_plugin(tmp_dir_path, test_root_path)
        yield tmp_dir_path / "bin" / "snow"


@pytest.fixture(autouse=True)
def isolate_default_config_location(monkeypatch, temp_dir):
    monkeypatch.setenv("SNOWFLAKE_HOME", temp_dir)


def _create_venv(tmp_dir: Path) -> None:
    subprocess.check_call(["python", "-m", "venv", tmp_dir])


def _build_snowcli(venv_path: Path, test_root_path: Path) -> None:
    subprocess.check_call(
        [_python_path(venv_path), "-m", "pip", "install", "--upgrade", "build"]
    )
    subprocess.check_call(
        [_python_path(venv_path), "-m", "build", test_root_path / ".."]
    )


def _pip_install(python, *args):
    return subprocess.check_call([python, "-m", "pip", "install", *args])


def _install_snowcli_with_external_plugin(
    venv_path: Path, test_root_path: Path
) -> None:
    version = __about__.VERSION
    python = _python_path(venv_path)
    _pip_install(
        python,
        test_root_path / f"../dist/snowflake_cli_labs-{version}-py3-none-any.whl",
    )
    _pip_install(
        python,
        test_root_path.parent
        / "test_external_plugins"
        / "multilingual_hello_command_group",
    )

    # Required by snowpark example tests
    _pip_install(python, "snowflake-snowpark-python")


def _python_path(venv_path: Path) -> Path:
    return venv_path / "bin" / "python"


# Inspired by project_directory fixture in tests_integration/conftest.py
# This is a simpler implementation of that fixture, i.e. does not include supporting local PDFs.
@pytest.fixture
def project_directory(temp_dir, test_root_path):
    @contextmanager
    def _temporary_project_directory(project_name):
        test_data_file = test_root_path / "test_data" / project_name
        shutil.copytree(test_data_file, temp_dir, dirs_exist_ok=True)
        yield Path(temp_dir)

    return _temporary_project_directory
