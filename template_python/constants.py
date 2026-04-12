"""Constants for codebases using this template."""

# Sphinx
SPHINX_EXTENSIONS = [
    "sphinx.ext.autodoc",  # Auto-generate API docs from docstrings
    "sphinx.ext.autosummary",  # Generate summary tables
    "sphinx.ext.napoleon",  # Support Google/NumPy style docstrings
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx.ext.intersphinx",  # Link to other project documentation
    "sphinx_autodoc_typehints",  # Better type hint rendering
    "sphinx_substitution_extensions",  # Support for substitutions in RST files
]
SPHINX_HTML_THEME = "furo"
