"""Utility script for GitHub workflows."""

import tomllib

from pyhere import here


def _load_pyproject() -> dict:
    """Load the pyproject.toml file."""
    with here("pyproject.toml").open("rb") as f:
        return tomllib.load(f)


def _load_uv_lock() -> dict:
    """Load the uv.lock file."""
    with here("uv.lock").open("rb") as f:
        return tomllib.load(f)


def get_version_pyproject() -> None:
    """Get the version from pyproject.toml."""
    pyproject = _load_pyproject()
    print(pyproject["project"]["version"])


def get_version_uv_lock() -> None:
    """Get the version from uv.lock."""
    pyproject = _load_pyproject()
    uv_lock = _load_uv_lock()
    pkg = next((p for p in uv_lock["package"] if p["name"] == pyproject["project"]["name"]), None)
    print(pkg["version"] if pkg else "not found")
