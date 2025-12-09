[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=ffd343)](https://docs.python.org/3.12/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![CI](https://img.shields.io/github/actions/workflow/status/javidahmed64592/template-python/ci.yml?branch=main&style=flat-square&label=CI&logo=github)](https://github.com/javidahmed64592/template-python/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- omit from toc -->
# Template Python Repository
This repository can be used as a template for a Python application.

<!-- omit from toc -->
## Table of Contents
- [uv](#uv)
- [Installing Dependencies](#installing-dependencies)
- [Testing, Linting, and Type Checking](#testing-linting-and-type-checking)
- [License](#license)

## uv
This repository is managed using the `uv` Python project manager: https://docs.astral.sh/uv/

To install `uv`:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh                                    # Linux/Mac
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" # Windows
```

## Installing Dependencies
Install the required dependencies using `uv`:

    uv sync

To install with `dev` dependencies:

    uv sync --extra dev

After installing dev dependencies, set up pre-commit hooks:

    uv run pre-commit install

## Testing, Linting, and Type Checking

- **Run all pre-commit checks:** `uv run pre-commit run --all-files`
- **Lint code:** `uv run ruff check .`
- **Format code:** `uv run ruff format .`
- **Type check:** `uv run mypy .`
- **Run tests:** `uv run pytest`
- **Security scan:** `uv run bandit -r example/`
- **Audit dependencies:** `uv run pip-audit`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
