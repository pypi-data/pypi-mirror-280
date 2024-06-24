import re
import os
import shutil
import subprocess

from create_api_app.conf.constants import BACKEND_CORE_PACKAGES, BACKEND_DEV_PACKAGES
from create_api_app.conf.constants.filepaths import (
    ProjectPaths,
    SetupAssetsDirNames,
    SetupDirPaths,
    set_poetry_version,
)
from create_api_app.conf.constants.content import PoetryContent
from create_api_app.conf.file_handler import insert_into_file, replace_content
from .base import ControllerBase


class VEnvController(ControllerBase):
    """A controller for creating a Python virtual environment."""

    def __init__(self, project_paths: ProjectPaths = None) -> None:
        tasks = [
            (
                self.install,
                "Installing [yellow]Poetry[/yellow]",
            ),
            (
                self.init_project,
                "Initalising [yellow]backend[/yellow] as a [green]Poetry[/green] project",
            ),
            (
                self.add_dependencies,
                "".join(
                    [
                        "Adding [green]core[/green] and [magenta]development[/magenta] [yellow]Poetry[/yellow] packages ->",
                        f"\n     - [green]{" ".join(BACKEND_CORE_PACKAGES)}[/green]",
                        f"\n     - [magenta]{" ".join(BACKEND_DEV_PACKAGES)}[/magenta]",
                    ]
                ),
            ),
            (
                self.update_toml,
                "Updating [yellow]pyproject.toml[/yellow] with build scripts",
            ),
        ]

        super().__init__(tasks, project_paths)

        self.poetry_content = PoetryContent()

    def install(self) -> None:
        """Installs a set of `PIP` packages."""
        subprocess.run(
            ["pip", "install", "poetry"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def init_project(self) -> None:
        """Creates a poetry project."""
        subprocess.run(
            ["poetry", "new", "app"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        os.rename(os.path.join(self.project_paths.ROOT, "app"), "backend")
        os.chdir(self.project_paths.BACKEND)

    def add_dependencies(self) -> None:
        """Adds PIP packages to the poetry project."""
        subprocess.run(
            ["poetry", "add", *BACKEND_CORE_PACKAGES],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        subprocess.run(
            ["poetry", "add", *BACKEND_DEV_PACKAGES, "--dev"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # Store poetry version
        pv_result = subprocess.run(
            ["poetry", "--version"], capture_output=True, text=True
        )
        set_poetry_version(re.search(r"\d+\.\d+\.\d+", pv_result.stdout).group(0))

    def update_toml(self) -> None:
        """Updates the `pyproject.toml` with specific information."""
        replace_content(
            'description = ""',
            self.poetry_content.pyproject_desc(),
            self.project_paths.POETRY_CONF,
        )

        replace_content(
            "rpartridge101@yahoo.co.uk",
            self.poetry_content.pyproject_author(),
            self.project_paths.POETRY_CONF,
        )

        insert_into_file(
            'readme = "README.md"',
            self.poetry_content.pyproject_scripts(),
            self.project_paths.POETRY_CONF,
        )

        os.chdir(self.project_paths.ROOT)


class BackendStaticAssetController(ControllerBase):
    """A controller for managing the backend static assets."""

    def __init__(self, project_paths: ProjectPaths = None) -> None:
        tasks = [
            (
                self.move_setup_assets,
                "Configuring [yellow]backend[/yellow] files",
            ),
        ]

        super().__init__(tasks, project_paths)

    def move_setup_assets(self) -> None:
        """Moves the items in the `setup_assets` folder into the project directory."""
        backend_path = os.path.join(os.getcwd(), SetupAssetsDirNames.BACKEND)
        shutil.copytree(SetupDirPaths.BACKEND_ASSETS, backend_path, dirs_exist_ok=True)

        shutil.copytree(SetupDirPaths.ROOT_ASSETS, os.getcwd(), dirs_exist_ok=True)
