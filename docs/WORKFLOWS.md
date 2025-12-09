# GitHub Workflows

This document details the CI/CD workflows for the template Python repository.
They run automated code quality checks to ensure code remains robust, maintainable, and testable.

## CI Workflow

The CI workflow runs on pushes and pull requests to the `main` branch.
It consists of the following jobs:

### validate-pyproject
  - Checkout code
  - Setup Python environment with dev dependencies (via custom action)
  - Validate `pyproject.toml` structure using `validate-pyproject`

### ruff
  - Checkout code
  - Setup Python environment with dev dependencies (via custom action)
  - Run Ruff linter with `uv run -m ruff check`

### mypy
  - Checkout code
  - Setup Python environment with dev dependencies (via custom action)
  - Run mypy type checking with `uv run -m mypy .`

### test
  - Checkout code
  - Setup Python environment with dev dependencies (via custom action)
  - Run pytest with coverage (HTML and terminal reports) using `uv run -m pytest --cov-report html --cov-report term`
  - Fails if coverage drops below 80% (configured in `pyproject.toml`)
  - Upload HTML coverage report as artifact

### bandit
  - Checkout code
  - Setup Python environment with dev dependencies (via custom action)
  - Run security scanning with bandit on `example/` directory
  - Generate JSON report for artifacts
  - Fail if security vulnerabilities are found

### pip-audit
  - Checkout code
  - Setup Python environment with dev dependencies (via custom action)
  - Audit dependencies for known CVEs using `pip-audit --desc`

### version-check
- **Runner**: Ubuntu Latest
- **Steps**:
  - Checkout code
  - Setup Python environment with dev dependencies (via custom action)
  - Check version consistency between `pyproject.toml` and `uv.lock`
  - Ensures the package version matches across both files
  - Fails if versions are mismatched

## Custom GitHub Actions

The workflow uses custom composite actions for environment setup:

### setup-python-dev
- **Location**: `.github/actions/setup-python-dev/action.yml`
- **Purpose**: Sets up Python with uv and installs all dev dependencies
- **Steps**:
  - Install uv with caching enabled
  - Setup Python from `.python-version` file
  - Run `uv sync --extra dev` to install dependencies

### setup-python-core
- **Location**: `.github/actions/setup-python-core/action.yml`
- **Purpose**: Sets up Python with uv and installs only core dependencies
- **Steps**:
  - Install uv with caching enabled
  - Setup Python from `.python-version` file
  - Run `uv sync` to install core dependencies only
