from .filepaths import AssetFilenames


class PoetryContent:
    """A helper class for retrieving content for the Poetry installation."""

    def __init__(self) -> None:
        self.START_SERVER_CMD = f"{AssetFilenames.BUILD.split('.')[0]}:start"

    def pyproject_desc(self) -> str:
        return 'description = "A FastAPI backend for processing API data and passing it to the frontend."'

    def pyproject_author(self) -> str:
        return "rpartridge101@gmail.com"

    def pyproject_scripts(self) -> str:
        return f'\n\n[tool.poetry.scripts]\nrun = "{self.START_SERVER_CMD}"\n\n'


class FrontendContent:
    """A helper class for retrieving content for the frontend installation."""

    def tailwind_font(self) -> str:
        """New content for the `Rubik` font in the tailwind config."""
        return "\n".join(
            [
                "extend: {",
                "      fontFamily: {",
                '        rubik: ["Rubik", "sans-serif"],',
                "      },",
            ]
        )
