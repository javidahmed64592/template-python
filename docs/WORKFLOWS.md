<!-- omit from toc -->
# GitHub Workflows

This document details the CI/CD workflows and reusable actions to build and release Python applications.
They run automated code quality checks to ensure code remains robust, maintainable, and testable.

- [Reusable Actions (`./github/actions`)](#reusable-actions-githubactions)
  - [Setup Actions (`/setup/**/action.yml`)](#setup-actions-setupactionyml)
  - [CI Actions (`/ci/**/action.yml`)](#ci-actions-ciactionyml)
  - [Build Actions (`/build/**/action.yml`)](#build-actions-buildactionyml)
- [Workflows (`./github/workflows`)](#workflows-githubworkflows)
  - [CI Workflow (`ci.yml`)](#ci-workflow-ciyml)
  - [Build Workflow (`build.yml`)](#build-workflow-buildyml)


## Reusable Actions (`./github/actions`)

The following actions can be referenced from other repositories using `javidahmed64592/template-python/.github/actions/{category}/{action}@main`.

### Setup Actions (`/setup/**/action.yml`)

**setup-uv-python:**
- Description: Sets up Python with uv.
- Location: `setup-uv-python/action.yml`
- Steps:
  - Installs uv using `astral-sh/setup-uv@v7` with caching enabled
  - Sets up Python using the version specified in `.python-version`
  - Caches dependencies based on `uv.lock` for faster builds

Usage:
```yaml
steps:
  - uses: javidahmed64592/template-python/.github/actions/setup/setup-uv-python@main
```

---

**install-python-core:**
- Description: Installs core Python dependencies from pyproject.toml using uv.
- Location: `install-python-core/action.yml`
- Steps:
  - Uses the `setup-uv-python` action
  - Runs `uv sync` to install only core dependencies

Usage:
```yaml
steps:
  - uses: javidahmed64592/template-python/.github/actions/setup/install-python-core@main
```

---

**install-python-dev:**
- Description: Installs dev Python dependencies from pyproject.toml using uv.
- Location: `install-python-dev/action.yml`
- Steps:
  - Uses the `setup-uv-python` action
  - Runs `uv sync --extra dev` to install core and dev dependencies
- Note: Requires `pyproject.toml` with dev dependencies defined under `[project.optional-dependencies]`.

Usage:
```yaml
steps:
  - uses: javidahmed64592/template-python/.github/actions/setup/install-python-dev@main
```

---

### CI Actions (`/ci/**/action.yml`)

**validate-pyproject:**
- Description: Validate pyproject.toml structure.
- Location: `validate-pyproject/action.yml`
- Steps:
  - Uses the `install-python-dev` action
  - Runs `uv run validate-pyproject pyproject.toml` to validate TOML structure

Usage:
```yaml
steps:
  - uses: javidahmed64592/template-python/.github/actions/ci/validate-pyproject@main
```

---

**ruff:**
- Description: Run Ruff linting checks on the codebase.
- Location: `ruff/action.yml`
- Steps:
  - Uses the `install-python-dev` action
  - Runs `uv run -m ruff check` to lint the code
- Note: Requires Ruff configuration in `pyproject.toml` under `[tool.ruff]`.

Usage:
```yaml
steps:
  - uses: javidahmed64592/template-python/.github/actions/ci/ruff@main
```

---

**mypy:**
- Description: Run Mypy type checking on the codebase.
- Location: `mypy/action.yml`
- Steps:
  - Uses the `install-python-dev` action
  - Runs `uv run -m mypy .` to perform static type checking
- Note: Requires Mypy configuration in `pyproject.toml` under `[tool.mypy]`.

Usage:
```yaml
steps:
  - uses: javidahmed64592/template-python/.github/actions/ci/mypy@main
```

---

**pytest:**
- Description: Run Pytest tests with coverage reporting.
- Location: `pytest/action.yml`
- Steps:
  - Uses the `install-python-dev` action
  - Runs `uv run -m pytest --cov-report html --cov-report term` to execute tests with coverage
  - Uploads HTML coverage report as artifact named `backend-coverage-report`
  - Fails if coverage drops below the threshold configured in `pyproject.toml`
- Note: Requires pytest and pytest-cov configuration in `pyproject.toml` under `[tool.pytest.ini_options]` and `[tool.coverage]`.

Usage:
```yaml
steps:
  - uses: javidahmed64592/template-python/.github/actions/ci/pytest@main
```

---

**bandit:**
- Description: Run Bandit security checks on the codebase.
- Location: `bandit/action.yml`
- Steps:
  - Uses the `install-python-dev` action
  - Runs `uv run bandit -r $PACKAGE_NAME -f json -o bandit-report.json` to scan for security vulnerabilities
  - Uploads JSON report as artifact named `bandit-report`
- Note: Requires `PACKAGE_NAME` environment variable to be set at the workflow or job level.

Usage:
```yaml
env:
  PACKAGE_NAME: your_package_name
steps:
  - uses: javidahmed64592/template-python/.github/actions/ci/bandit@main
```

---

**pip-audit:**
- Description: Run pip-audit to check for known vulnerabilities in dependencies.
- Location: `pip-audit/action.yml`
- Steps:
  - Uses the `install-python-dev` action
  - Runs `uv run pip-audit --desc` to check dependencies for known CVEs

Usage:
```yaml
steps:
  - uses: javidahmed64592/template-python/.github/actions/ci/pip-audit@main
```

---

**version-check:**
- Description: Check version consistency across pyproject.toml and uv.lock.
- Location: `version-check/action.yml`
- Steps:
  - Uses the `install-python-dev` action
  - Extracts version from `pyproject.toml` using `uv run ci-version-pyproject`
  - Verifies `uv.lock` version matches using `uv run ci-version-uv-lock`
  - Optionally checks additional version files via `additional-versions` input
  - Fails if any version mismatch is detected

Usage:
```yaml
steps:
  - uses: javidahmed64592/template-python/.github/actions/ci/version-check@main
```

Advanced usage with additional version files:
```yaml
steps:
  - uses: javidahmed64592/template-python/.github/actions/ci/version-check@main
    with:
      additional-versions: '[{"name": "package.json", "version": "1.2.3"}]'
```

---

### Build Actions (`/build/**/action.yml`)

**build-wheel:**
- Description: Build Python wheel package and upload as artifact.
- Location: `build-wheel/action.yml`
- Steps:
  - Uses the `install-python-core` action
  - Runs `uv build` to create the wheel
  - Inspects wheel contents using `unzip -l`
  - Uploads wheel as artifact with name `{PACKAGE_NAME}_wheel`
- Note: Requires `PACKAGE_NAME` environment variable and build configuration in `pyproject.toml` under `[build-system]`.

Usage:
```yaml
env:
  PACKAGE_NAME: your_package_name
steps:
  - uses: javidahmed64592/template-python/.github/actions/build/build-wheel@main
```

---

**verify-structure:**
- Description: Download and verify the structure of the built wheel package.
- Location: `verify-structure/action.yml`
- Steps:
  - Uses the `install-python-core` action
  - Downloads the wheel artifact (named `{PACKAGE_NAME}_wheel`)
  - Installs the wheel using `uv pip install`
  - Verifies that the package directory exists in site-packages
  - Fails if required package structure is missing
- Note: Requires `PACKAGE_NAME` environment variable. Should run after `build-wheel` action using `needs: build-wheel` at the job level.

Usage:
```yaml
env:
  PACKAGE_NAME: your_package_name
steps:
  - uses: javidahmed64592/template-python/.github/actions/build/verify-structure@main
```

## Workflows (`./github/workflows`)

The following workflows ensure Python codebases are robust and thoroughly tested.

### CI Workflow (`ci.yml`)

The CI workflow runs on pushes and pull requests to the `main` branch.
It runs 7 parallel jobs to validate code quality, security, and consistency.

**Jobs:**
- `validate-pyproject` - Validates `pyproject.toml` structure
- `ruff` - Runs Ruff linting checks
- `mypy` - Runs static type checking
- `pytest` - Runs tests with coverage reporting
- `bandit` - Scans for security vulnerabilities
- `pip-audit` - Audits dependencies for known CVEs
- `version-check` - Verifies version consistency

### Build Workflow (`build.yml`)

The Build workflow runs on pushes and pull requests to the `main` branch.
It builds and verifies the Python wheel package.

**Jobs:**
- `build-wheel` - Builds the wheel package and uploads as artifact
- `verify-structure` - Downloads and verifies the wheel contents (depends on `build-wheel`)
