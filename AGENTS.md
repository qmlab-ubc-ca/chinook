# Repository Guidelines

## Project Structure & Module Organization

Core Python code lives in `chinook/`. Modules such as `TB_lib.py`, `ARPES_lib.py`, and `SlaterKoster.py` implement tight-binding and ARPES calculations; packaged reference data is stored beside them in `*.txt` files. Runnable workflows and sample inputs belong in `examples/`. Sphinx documentation is under `docs/source/`, with images in `docs/source/images/` and downloadable tutorial files in `docs/source/downloads/`. Packaging metadata is maintained in `setup.py`, `requirements.txt`, and `MANIFEST.in`.

## Build, Test, and Development Commands

- `python -m venv .venv && source .venv/bin/activate` creates an isolated environment.
- `python -m pip install -e .` installs Chinook and its NumPy, SciPy, and Matplotlib dependencies in editable mode.
- `python -m compileall chinook` performs a quick syntax check across the package.
- `python examples/template.py` runs the main starter example; run other example scripts when changing their related physics workflow.
- `make -C docs html` builds the Sphinx HTML documentation into `docs/build/html/` (requires Sphinx and `sphinx-rtd-theme`).

## Coding Style & Naming Conventions

Use Python 3.9-compatible syntax, four-space indentation, UTF-8 text, and PEP 8 spacing. Prefer `snake_case` for new functions, variables, and modules, and `PascalCase` for classes. Existing mixed-case module names are part of the historical API; do not rename them casually. Add concise docstrings to public functions and document array shapes, units, and coordinate conventions. Keep numerical changes focused and avoid unrelated reformatting. No formatter or linter is configured, so match the surrounding file.

## Testing Guidelines

There is currently no committed automated test suite or coverage requirement. For bug fixes and new behavior, add focused `pytest` tests under `tests/`, named `test_<module>.py`, with test functions named `test_<behavior>()`. Use small deterministic arrays and explicit tolerances (`numpy.testing.assert_allclose`) for floating-point results. Until a suite exists, report the syntax check and relevant example scripts run in the pull request.

## Commit & Pull Request Guidelines

Recent history commonly uses short imperative subjects and Conventional Commit prefixes such as `fix:` and `feat:`. Follow that pattern, for example `fix: preserve orbital ordering in slab model`. Keep commits scoped to one logical change. Pull requests should explain the motivation and numerical or user-visible impact, list validation commands, and link related issues. Include plots or screenshots when output figures or documentation rendering changes; call out compatibility or packaged-data changes explicitly.
