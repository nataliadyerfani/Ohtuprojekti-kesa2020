[![CircleCI](https://circleci.com/gh/kordaniel/Ohtuprojekti-kesa2020.svg?style=svg)](https://circleci.com/gh/kordaniel/Ohtuprojekti-kesa2020)

[![codecov](https://codecov.io/gh/kordaniel/Ohtuprojekti-kesa2020/branch/master/graph/badge.svg)](https://codecov.io/gh/kordaniel/Ohtuprojekti-kesa2020)

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
'-c camera_id'

# Testing
Unit testing with python builtin unittest library. Run with:
```console
cd tests
python3 -m unittest
```
Add -v flag for verbose output  
Run single test module:
```console
cd tests
python3 -m unittest modulename
```
Run all modules in a directory called tests:
```console
python3 -m unittest discover -s tests
```

# Formatting
Run [yapf](https://github.com/google/yapf/) before commits `yapf -ri src/`

[pep8 style guide](https://www.python.org/dev/peps/pep-0008/)
