# python-language-tester
Repo for testing features of the Python 3 language.

## Set up
1. Add `pip` to PATH (usually in `Scripts` folder in Python installation directory.
2. Install dependencies using:
   ```
   pip install --upgrade pip
   pip install poetry
   poetry install --no-root
   ```

## Running
Can run unit tests using:
```
pip install pytest

# Not sure why this is needed but otherwise tests will fail on the command line
pip install numpy

pytest
```
