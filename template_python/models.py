"""Pydantic models used across the codebase."""

from datetime import datetime

from pydantic import BaseModel, Field


class SphinxConfig(BaseModel):
    """Configuration for Sphinx documentation generation."""

    repo_name: str = Field(..., description="The name of the repository.")
    version: str = Field(..., description="The version of the project.")
    author: str = Field(..., description="The author of the project.")
    extensions: list[str] = Field(default_factory=list, description="List of Sphinx extensions to use.")
    html_theme: str = Field(..., description="The HTML theme to use for Sphinx documentation.")

    @property
    def project_name(self) -> str:
        """Generate a human-readable project name from the repository name."""
        return self.repo_name.replace("-", " ").title()

    @property
    def package_name(self) -> str:
        """Generate a valid Python package name from the repository name."""
        return self.repo_name.replace("-", "_")

    @property
    def copyright(self) -> str:
        """Generate a copyright string using the current year and author."""
        return f"{datetime.now().year}, {self.author}"

    @property
    def rst_prolog_keys(self) -> list[str]:
        """Get the keys for RST substitutions."""
        return ["project_name", "package_name", "repo_name"]

    @property
    def rst_prolog_values(self) -> list[str]:
        """Get the values for RST substitutions."""
        return [self.project_name, self.package_name, self.repo_name]
