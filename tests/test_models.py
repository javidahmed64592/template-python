"""Unit tests for the template_python.models module."""

from template_python.models import SphinxConfig


class TestSphinxConfig:
    """Tests for the SphinxConfig model."""

    def test_sphinx_config_properties(self) -> None:
        """Test the properties of the SphinxConfig model."""
        repo_name = "template-python"
        version = "0.1.0"
        author = "Author Name"
        extensions = ["extension1", "extension2"]
        theme = "theme"

        config = SphinxConfig(
            repo_name=repo_name,
            version=version,
            author=author,
            extensions=extensions,
            html_theme=theme,
        )

        assert isinstance(config.project_name, str)
        assert isinstance(config.package_name, str)
        assert isinstance(config.copyright, str)
        assert isinstance(config.rst_prolog_keys, list)
        assert isinstance(config.rst_prolog_values, list)
