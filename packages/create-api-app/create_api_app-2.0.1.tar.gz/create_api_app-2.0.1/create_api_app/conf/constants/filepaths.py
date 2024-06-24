import os

from create_api_app.utils.helper import get_dirpaths


class SetupAssetsDirNames:
    """A storage container for setup asset directory names."""

    ROOT = "setup_assets"
    FRONTEND = "frontend"
    BACKEND = "backend"
    APP = "app"


class AssetFilenames:
    """A storage container for asset filenames."""

    POETRY_CONF = "pyproject.toml"
    README = "README.md"

    MAIN = "main.py"
    BUILD = "build.py"

    TAILWIND = "tailwind.config.ts"
    NEXT_CONFIG = "next.config.mjs"


class SetupDirPaths:
    """A storage container for setup asset filepaths."""

    DIRPATHS_DICT = get_dirpaths("create_api_app", "setup_assets")

    BACKEND_ASSETS = DIRPATHS_DICT[SetupAssetsDirNames.BACKEND]
    FRONTEND_ASSETS = DIRPATHS_DICT[SetupAssetsDirNames.FRONTEND]
    ROOT_ASSETS = DIRPATHS_DICT["root"]


def __dotenv_setter(name: str, value: str) -> None:
    os.environ[name] = value


def set_project_name(name: str) -> None:
    __dotenv_setter("PROJECT_NAME", name)


def set_poetry_version(version: str) -> None:
    __dotenv_setter("POETRY_VERSION", version)


def get_project_name() -> str:
    return os.environ.get("PROJECT_NAME")


def get_poetry_version() -> str:
    return os.environ.get("POETRY_VERSION")


class ProjectPaths:
    """A storage container for project directory and filename paths."""

    def __init__(self, project_name: str = None) -> None:
        self.PROJECT_NAME = project_name if project_name else get_project_name()
        self.ROOT = os.path.join(os.path.dirname(os.getcwd()), self.PROJECT_NAME)
        self.BACKEND = os.path.join(self.ROOT, SetupAssetsDirNames.BACKEND)
        self.BACKEND_APP = os.path.join(self.BACKEND, SetupAssetsDirNames.APP)
        self.FRONTEND = os.path.join(self.ROOT, SetupAssetsDirNames.FRONTEND)

        self.POETRY_CONF = os.path.join(self.BACKEND, AssetFilenames.POETRY_CONF)

        self.TAILWIND_CONF = os.path.join(self.FRONTEND, AssetFilenames.TAILWIND)
