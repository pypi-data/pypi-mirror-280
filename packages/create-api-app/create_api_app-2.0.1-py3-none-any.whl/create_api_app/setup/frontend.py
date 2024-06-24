import os
import shutil
import subprocess

from create_api_app.conf.constants.content import FrontendContent
from create_api_app.conf.constants.filepaths import (
    ProjectPaths,
    SetupAssetsDirNames,
    SetupDirPaths,
)
from create_api_app.conf.file_handler import replace_content
from .base import ControllerBase


class NextJSController(ControllerBase):
    """A controller for creating the Next.js assets."""

    def __init__(self, project_paths: ProjectPaths = None) -> None:
        tasks = [
            (
                self.install,
                "Creating [green]Next.js[/green] project",
            ),
        ]

        super().__init__(tasks, project_paths)

    def install(self) -> None:
        """Creates the Next.js files."""
        subprocess.run(["build-nextjs-app", "frontend"])


class FrontendStaticAssetController(ControllerBase):
    """A controller for managing the frontend static assets."""

    def __init__(self, project_paths: ProjectPaths = None) -> None:
        tasks = [
            (
                self.add_folders,
                "Updating [green]project[/green] structure",
            ),
            (
                self.update_files,
                "Updating [green]core[/green] files and adding [green]new[/green] ones",
            ),
        ]

        super().__init__(tasks, project_paths)

        self.content = FrontendContent()

        self.src_path = os.path.join(os.getcwd(), SetupAssetsDirNames.FRONTEND, "src")
        self.frontend_path = os.path.join(os.getcwd(), SetupAssetsDirNames.FRONTEND)

    def add_folders(self) -> None:
        """Add empty folders to the frontend."""
        dir_paths = [
            os.path.join(self.src_path, "components"),
            os.path.join(self.src_path, "data"),
            os.path.join(self.src_path, "hooks"),
            os.path.join(self.src_path, "layouts"),
            os.path.join(self.src_path, "pages"),
            os.path.join(self.src_path, "types"),
        ]

        for directory in dir_paths:
            os.makedirs(directory, exist_ok=True)

    def update_files(self) -> None:
        """Replaces frontend files with new ones."""
        shutil.copytree(
            SetupDirPaths.FRONTEND_ASSETS, self.frontend_path, dirs_exist_ok=True
        )

        replace_content(
            old="extend: {",
            new=self.content.tailwind_font(),
            path=self.project_paths.TAILWIND_CONF,
        )
