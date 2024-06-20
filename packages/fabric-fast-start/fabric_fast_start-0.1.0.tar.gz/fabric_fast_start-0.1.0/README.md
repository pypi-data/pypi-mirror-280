# Python package template

This is a template repository for any Python package that comes with the following dev tools:

* `ruff`: identifies many errors and style issues (`flake8`, `isort`, `pyupgrade`)
* `black`: auto-formats code
* `mypy`: static type checker

Those checks are run as pre-commit hooks using the `pre-commit` library.

It includes `pytest` for testing plus the `pytest-cov` plugin to measure coverage.

The checks and tests are all run using Github actions on every pull request and merge to main.

This repository is setup for Python 3.12. To change the version:

1. Change the `image` argument in `.devcontainer/devcontainer.json` (see [https://github.com/devcontainers/images/tree/main/src/python](https://github.com/devcontainers/images/tree/main/src/python#configuration) for a list of pre-built Docker images)
1. Change the config options in `.precommit-config.yaml`
1. Change the config options in `.pyproject.toml`
1. Change the version number in `.github/workflows/`

## Development instructions

## With devcontainer

This repository comes with a devcontainer (a Dockerized Python environment). If you open it in Codespaces, it should automatically initialize the devcontainer.

Locally, you can open it in VS Code with the Dev Containers extension installed.

## Without devcontainer

If you can't or don't want to use the devcontainer, then you should first create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then install the dev tools and pre-commit hooks:

```bash
python3 -m pip install -e '.[dev]'
pre-commit install
```

## Adding code and tests

This repository starts with a very simple `main.py` and a test for it at `tests/test_main_module.py`.
You'll want to replace that with your own code, and you'll probably want to add additional files
as your code grows in complexity.

When you're ready to run tests, run:

```bash
python3 -m pytest
```

## File breakdown

Here's a short explanation of each file/folder in this template:

* `.devcontainer`: Folder containing files used for setting up a devcontainer
  * `devcontainer.json`: File configuring the devcontainer, includes VS Code settings
* `.github`: Folder for Github-specific files and folders
  * `workflows`: Folder containing Github actions config files
* `tests`: Folder containing Python tests
  * `test_main_module.py`: File with pytest-style tests of main.py
* `.gitignore`: File describing what file patterns Git should never track
* `.pre-commit-config.yaml`: File listing all the pre-commit hooks and args
* `src`: Folder containing the source files for your Python package.
  * `fabric-fast-start`: Folder containing the package.
    * `py.typed`: File to force mypy to analyze package types.
    * `__init__.py`: File to specify that this is a Python module.
    * `main.py`: The main (and currently only) Python file for the program.
* `CHANGELOG.md`: File to log the significant changes to the package between releases.
* `pyproject.toml`: File configuring most of the Python dev tools
* `README.md`: You're reading it!

## 🔎 Found an issue or have an idea for improvement?

Help me make this template repository better by letting me know and opening an issue!
