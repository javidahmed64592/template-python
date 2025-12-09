# Python Template Project - AI Agent Instructions

## Project Overview

This is a template Python repository demonstrating modern Python tooling with `uv`, `ruff`, `mypy`, and `pytest`. The project uses Python 3.12+ and follows strict type checking and linting standards.

## Package Management with uv

- **Always use `uv` commands**, not `pip` - this project is managed exclusively with `uv`
- Install dependencies: `uv sync` (core) or `uv sync --extra dev` (with dev tools)
- Run commands: `uv run <command>` (e.g., `uv run pytest`, `uv run mypy .`)
- Update dependencies: `uv lock --upgrade`
- Version pinned in `.python-version` (currently 3.12)

## Code Quality Standards

### Ruff Configuration (pyproject.toml)

- Line length: 120 characters
- Target: Python 3.12
- Extensive rule selection including: type annotations (ANN), docstrings (D), performance (PERF), pandas (PD), numpy (NPY)
- **Ignored rules**: D203, D213 (conflicting docstring rules), PLR0913 (too many arguments), S101 (assert allowed in tests)
- `__init__.py` files excluded from linting via `extend-exclude`

### Type Checking (mypy)

- Strict configuration: `disallow_incomplete_defs`, `check_untyped_defs`, `warn_return_any`
- NumPy imports ignore missing type stubs via `[[tool.mypy.overrides]]`
- **All functions require type annotations** - never omit return types or parameter types

### Testing (pytest)

- Configuration in `pyproject.toml` under `[tool.pytest.ini_options]`
- Always run with coverage: `uv run pytest` (coverage enabled by default via `addopts`)
- Coverage report format: `term-missing` shows uncovered lines
- Test files in `tests/` directory follow `test_*.py` naming

## Development Workflow

### Before Committing

1. Format: `uv run ruff format .`
2. Lint: `uv run ruff check .`
3. Type check: `uv run mypy .`
4. Test: `uv run pytest`

### CI Pipeline (.github/workflows/ci.yml)

The CI runs 5 jobs in parallel:

1. `validate-pyproject` - validates pyproject.toml structure with `validate-pyproject`
2. `ruff` - linting with `uv run -m ruff check`
3. `mypy` - type checking with `uv run -m mypy .`
4. `test` - pytest with HTML coverage report (uploaded as artifact)
5. `version-check` - ensures version consistency between `pyproject.toml` and `uv.lock`

**Note**: CI uses custom composite actions in `.github/actions/` for environment setup:

- `setup-python-dev` - installs Python + uv + dev dependencies
- `setup-python-core` - installs Python + uv + core dependencies only

## Code Style Patterns

### Module Documentation

Every Python file starts with a module-level docstring:

```python
"""Brief description of module purpose."""
```

### Function Signatures

Always include complete type annotations:

```python
def example_function() -> str:
    """Return a string."""
    return "This is an example function."
```

### Test Structure

Tests mirror the source structure and use descriptive names:

```python
def test_example_function() -> None:
    """Test the example_function."""
    result = example_function()
    assert result == "This is an example function."
```

## Project Structure

- `example/` - main package code
- `tests/` - pytest test files
- `pyproject.toml` - single source of truth for all configuration (build, dependencies, tooling)
- `uv.lock` - locked dependency versions
- `.python-version` - Python version specification for `uv` and CI

## Version Management

- Package version defined in `pyproject.toml` under `[project]` → `version`
- CI validates version consistency across `pyproject.toml` and `uv.lock`
- Update package name in CI's version-check job if renaming from "example"
