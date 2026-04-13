"""Utility script for GitHub workflows."""

import tomllib
from functools import cache

from pyhere import here

from template_python.constants import SPHINX_EXTENSIONS, SPHINX_HTML_THEME
from template_python.models import SphinxConfig


@cache
def _load_pyproject() -> dict:
    """Load the `pyproject.toml` file."""
    with here("pyproject.toml").open("rb") as f:
        return tomllib.load(f)


@cache
def _load_uv_lock() -> dict:
    """Load the `uv.lock` file."""
    with here("uv.lock").open("rb") as f:
        return tomllib.load(f)


@cache
def get_version_from_pyproject() -> str:
    """Get the version from `pyproject.toml`."""
    pyproject = _load_pyproject()
    return str(pyproject["project"]["version"])


@cache
def get_name_from_pyproject() -> str:
    """Get the name from `pyproject.toml`."""
    pyproject = _load_pyproject()
    return str(pyproject["project"]["name"])


@cache
def get_author_from_pyproject() -> str:
    """Get the author from `pyproject.toml`."""
    pyproject = _load_pyproject()
    authors = pyproject["project"]["authors"]
    if not authors:
        error_msg = "No authors found in `pyproject.toml`. Please add at least one author to the [project] section."
        raise ValueError(error_msg)
    return str(authors[0]["name"])


@cache
def get_version_from_uv_lock() -> str:
    """Get the version from `uv.lock`."""
    name = get_name_from_pyproject()
    uv_lock = _load_uv_lock()
    if pkg := next((p for p in uv_lock["package"] if p["name"] == name), None):
        return str(pkg["version"])

    error_msg = f"Package '{name}' not found in `uv.lock`"
    raise ValueError(error_msg)


def get_rst_prolog(keys: list[str], values: list[str]) -> str:
    """Generate an RST prolog with the given keys and values."""
    if len(keys) != len(values):
        error_msg = "Keys and values must have the same length."
        raise ValueError(error_msg)
    return "\n".join(f".. |{k}| replace:: {v}" for k, v in zip(keys, values, strict=False))


def get_sphinx_config() -> SphinxConfig:
    """Get the Sphinx configuration from `pyproject.toml`."""
    return SphinxConfig(
        repo_name=get_name_from_pyproject(),
        version=get_version_from_pyproject(),
        author=get_author_from_pyproject(),
        extensions=SPHINX_EXTENSIONS,
        html_theme=SPHINX_HTML_THEME,
    )


def print_version_pyproject() -> None:
    """Run `ci-pyproject-version` to echo the version from `pyproject.toml`."""
    print(get_version_from_pyproject())


def print_name_pyproject() -> None:
    """Run `ci-pyproject-name` to echo the name from `pyproject.toml`."""
    print(get_name_from_pyproject())


def print_version_uv_lock() -> None:
    """Run `ci-uv-lock-version` to echo the version from `uv.lock`."""
    print(get_version_from_uv_lock())
