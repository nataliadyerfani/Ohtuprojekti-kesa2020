[![CircleCI](https://circleci.com/gh/kordaniel/Ohtuprojekti-kesa2020.svg?style=svg)](https://circleci.com/gh/kordaniel/Ohtuprojekti-kesa2020) [![codecov](https://codecov.io/gh/kordaniel/Ohtuprojekti-kesa2020/branch/master/graph/badge.svg)](https://codecov.io/gh/kordaniel/Ohtuprojekti-kesa2020)

## Commands for virtual environment
[pipenv](https://github.com/pypa/pipenv) is used for managing dependencies

#### Creating virtual environment
`pipenv install`

#### Activate virtual environment
`pipenv shell`
or `pipenv run <command>` to run a single command in the environment
#### More
[pipenv usage](https://github.com/pypa/pipenv#-usage)

## Start main.py
`python src/main.py`

# Arguments for live_detect.py

## Define tensorflow model (default: detect.tflite)

`-m modelname.tflite`

## Define labelmap for model (default: labelmap.txt)

`-l labelmap.txt`

## Define a webcamera's ID (default: 0)
`-c camera_id`

# Testing
Run all tests from root folder:
```console
python -m unittest
```
Add -v flag after `unittest` for verbose output  

Run tests and generate coverage report
```console
coverage run -m unittest discover
coverage html
```

# Create test

Create test file named `test_<module_to_test>.py` and empty file called `__init__.py` side by side in `tests` folder or any of it's subfolders.

# Formatting
Run [yapf](https://github.com/google/yapf/) before commits `pipenv run yapf -ri src/`

[pep8 style guide](https://www.python.org/dev/peps/pep-0008/)