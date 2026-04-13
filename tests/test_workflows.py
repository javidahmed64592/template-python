"""Unit tests for the template_python.workflows module."""

from unittest.mock import patch

import pytest

from template_python.models import SphinxConfig
from template_python.workflows import (
    _load_pyproject,
    _load_uv_lock,
    get_author_from_pyproject,
    get_name_from_pyproject,
    get_rst_prolog,
    get_sphinx_config,
    get_version_from_pyproject,
    get_version_from_uv_lock,
    print_name_pyproject,
    print_version_pyproject,
    print_version_uv_lock,
)


class TestWorkflows:
    """Tests for the workflow utility functions."""

    def test_load_pyproject(self) -> None:
        """Test loading the `pyproject.toml` file."""
        pyproject = _load_pyproject()
        assert "project" in pyproject
        assert "name" in pyproject["project"]
        assert "version" in pyproject["project"]

    def test_load_uv_lock(self) -> None:
        """Test loading the `uv.lock` file."""
        name = get_name_from_pyproject()
        uv_lock = _load_uv_lock()
        assert "package" in uv_lock
        assert any(p["name"] == name for p in uv_lock["package"])

    def test_get_version_from_pyproject(self) -> None:
        """Test getting the version from `pyproject.toml`."""
        version = get_version_from_pyproject()
        assert isinstance(version, str)

    def test_get_name_from_pyproject(self) -> None:
        """Test getting the name from `pyproject.toml`."""
        name = get_name_from_pyproject()
        assert isinstance(name, str)

    def test_get_author_from_pyproject(self) -> None:
        """Test getting the author from `pyproject.toml`."""
        author = get_author_from_pyproject()
        assert isinstance(author, str)

    def test_get_author_from_pyproject_no_authors(self) -> None:
        """Test getting the author from `pyproject.toml` when no authors are defined."""
        get_author_from_pyproject.cache_clear()

        with patch("template_python.workflows._load_pyproject", return_value={"project": {"authors": []}}):
            with pytest.raises(ValueError, match=r"No authors found in `pyproject.toml`."):
                get_author_from_pyproject()

    def test_get_version_from_uv_lock(self) -> None:
        """Test getting the version from `uv.lock`."""
        version = get_version_from_uv_lock()
        assert isinstance(version, str)

    def test_get_version_from_uv_lock_not_found(self) -> None:
        """Test getting the version from `uv.lock` when the package is not found."""
        pyproject = _load_pyproject()

        get_version_from_uv_lock.cache_clear()

        with (
            patch("template_python.workflows._load_uv_lock", return_value={"package": []}),
            pytest.raises(ValueError, match=rf"Package '{pyproject['project']['name']}' not found in `uv.lock`"),
        ):
            get_version_from_uv_lock()

    def test_get_rst_prolog(self) -> None:
        """Test generating an RST prolog."""
        keys = ["key1", "key2"]
        values = ["value1", "value2"]
        prolog = get_rst_prolog(keys, values)
        expected_prolog = ".. |key1| replace:: value1\n.. |key2| replace:: value2"
        assert prolog == expected_prolog

    def test_get_rst_prolog_mismatched_keys_values(self) -> None:
        """Test generating an RST prolog with mismatched keys and values."""
        keys = ["key1", "key2"]
        values = ["value1"]
        with pytest.raises(ValueError, match=r"Keys and values must have the same length."):
            get_rst_prolog(keys, values)

    def test_get_sphinx_config(self) -> None:
        """Test getting the Sphinx configuration."""
        config = get_sphinx_config()
        assert isinstance(config, SphinxConfig)

    def test_print_version_pyproject(self) -> None:
        """Test printing the version from `pyproject.toml`."""
        print_version_pyproject()

    def test_print_name_pyproject(self) -> None:
        """Test printing the name from `pyproject.toml`."""
        print_name_pyproject()

    def test_print_version_uv_lock(self) -> None:
        """Test printing the version from `uv.lock`."""
        print_version_uv_lock()
