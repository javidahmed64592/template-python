<!-- omit from toc -->
# Software Maintenance Guide

This document outlines how to configure and setup a development environment to work on Python applications using this template.

**TEMPLATE NOTE:** This guide is configured for the `template-python` project. Update package names and examples for your specific project.

- [Backend (Python)](#backend-python)
  - [Installing Dependencies](#installing-dependencies)
  - [Testing, Linting, and Type Checking](#testing-linting-and-type-checking)
  - [Building Documentation](#building-documentation)

## Backend (Python)

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=ffd343)](https://docs.python.org/3.13/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&style=flat-square)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square)](https://github.com/astral-sh/ruff)

### Installing Dependencies

This repository is managed using the `uv` Python project manager: https://docs.astral.sh/uv/

Install the required dependencies:

```sh
uv sync
```

To include extra dependencies:

```sh
uv sync --extra dev
uv sync --extra docs
uv sync --all-extras
```

### Testing, Linting, and Type Checking

- **Run all pre-commit checks:** `uv run pre-commit run --all-files`
- **Lint code:** `uv run ruff check .`
- **Format code:** `uv run ruff format .`
- **Type check:** `uv run mypy .`
- **Run tests:** `uv run pytest`
- **Security scan:** `uv run bandit -r template_python/`  *(TEMPLATE NOTE: Update package name)*
- **Audit dependencies:** `uv run pip-audit`

### Building Documentation

This project uses Sphinx for documentation. To build the documentation:

```sh
uv run sphinx-build -M html docs/source/ docs/build/
```

The built documentation will be available at `docs/build/html/index.html`.
