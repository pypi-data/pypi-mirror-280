import importlib.resources as pkg_resources
from pathlib import Path


def strip_whitespace_and_dashes(name: str) -> str:
    """Replaces whitespace and dashes with '_' for a given `name` and returns the updated version."""
    name_split = []

    if "-" in name:
        name_split = name.split("-")
    elif " " in name:
        name_split = name.split(" ")

    if len(name_split) != 0:
        name = "_".join(name_split)

    return name.strip()


def get_dirpaths(package: str, resource_dir: str) -> dict[str, Path]:
    """List all files in the resource directory of the package and store them in a dictionary."""
    dirnames = {}
    for item in pkg_resources.files(package).joinpath(resource_dir).iterdir():
        dirnames[str(item).split("\\")[-1]] = item

    return dirnames
