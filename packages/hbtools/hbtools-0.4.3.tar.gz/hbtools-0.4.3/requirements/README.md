### Requirements generation

The requirements can be re-generated with the following commands
```console
pip-compile --output-file=requirements/requirements.txt --resolver=backtracking pyproject.toml --generate-hashes
pip-compile --extra=terminal --output-file=requirements/requirements-terminal.txt --resolver=backtracking pyproject.toml --generate-hashes
pip-compile --extra=test --output-file=requirements/requirements-test.txt --resolver=backtracking pyproject.toml --generate-hashes
pip-compile --extra=dev --output-file=requirements/requirements-dev.txt --resolver=backtracking pyproject.toml --generate-hashes
pip-compile --extra=build --output-file=requirements/requirements-build.txt --resolver=backtracking pyproject.toml --generate-hashes
pip-compile --extra=flake8 --output-file=requirements/requirements-flake8.txt --resolver=backtracking pyproject.toml --generate-hashes
```

Dependencies can be updated with:
```console
pip-compile --output-file=requirements/requirements.txt --resolver=backtracking pyproject.toml --generate-hashes --upgrade
pip-compile --extra=terminal --output-file=requirements/requirements-terminal.txt --resolver=backtracking pyproject.toml --generate-hashes --upgrade
pip-compile --extra=test --output-file=requirements/requirements-test.txt --resolver=backtracking pyproject.toml --generate-hashes --upgrade
pip-compile --extra=dev --output-file=requirements/requirements-dev.txt --resolver=backtracking pyproject.toml --generate-hashes --upgrade
pip-compile --extra=build --output-file=requirements/requirements-build.txt --resolver=backtracking pyproject.toml --generate-hashes --upgrade
pip-compile --extra=flake8 --output-file=requirements/requirements-flake8.txt --resolver=backtracking pyproject.toml --generate-hashes --upgrade
```

Install the requirements with:
```console
pip install -r requirements/requirements.txt
pip install -r requirements/requirements-terminal.txt
pip install -r requirements/requirements-test.txt
pip install -r requirements/requirements-dev.txt
pip install -r requirements/requirements-build.txt
pip install -r requirements/requirements-flake8.txt
```
