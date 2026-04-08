"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import sys
from datetime import datetime
from pathlib import Path

from template_python.workflows import (
    _get_author_pyproject,
    _get_description_pyproject,
    _get_name_pyproject,
    _get_version_pyproject,
)

# Add the project root to sys.path for autodoc
sys.path.insert(0, str(Path(__file__).parents[2].resolve()))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# TEMPLATE NOTE: Update these values for your specific project

project = _get_name_pyproject().replace("-", " ").title()
copyright = f"{datetime.now().year}, {_get_author_pyproject()}"  # noqa: A001
author = _get_author_pyproject()
release = _get_version_pyproject()
package_name = _get_name_pyproject().replace("-", "_")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Auto-generate API docs from docstrings
    "sphinx.ext.autosummary",  # Generate summary tables
    "sphinx.ext.napoleon",  # Support Google/NumPy style docstrings
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx.ext.intersphinx",  # Link to other project documentation
    "myst_parser",  # Markdown support
    "sphinx_autodoc_typehints",  # Better type hint rendering
]

# Napoleon settings for Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Autodoc settings
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"

# Autosummary settings
autosummary_generate = True

# MyST parser settings (Markdown support)
myst_enable_extensions = [
    "colon_fence",  # ::: fences
    "deflist",  # Definition lists
    "html_image",  # HTML images
    "linkify",  # Auto-link URLs
    "replacements",  # Text replacements
    "smartquotes",  # Smart quotes
    "tasklist",  # Task lists [ ]
]
myst_heading_anchors = 3

# Intersphinx mapping to link to other projects
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

templates_path = ["_templates"]
exclude_patterns: list[str] = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# Theme options
html_theme_options = {
    "description": _get_description_pyproject(),
    "github_user": "javidahmed64592",  # TEMPLATE NOTE: Update for your GitHub username
    "github_repo": _get_name_pyproject(),
    "github_button": True,
    "github_banner": True,
    "show_powered_by": False,
    "show_related": False,
}
