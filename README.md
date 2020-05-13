# Commands for virtual environment

## Create virtuan environment
`python3 -m venv env`

## Activate virtual environment
`source env/bin/activate`

## Install packages from requirements.txt
`pip install -r requirements.txt`

## Install more packages/libraries to the environment
`pip install package_name==version-num`
or
`pip install package_name`

## Start main.py
`python3 src/main.py`

## Save requirements to file (freeze)
`pip freeze > requirements.txt`

## Leave virtual environment
`deactivate`

# Arguments for live_detect.py

## Define tensorflow model (default: detect.tflite)

`-m modelname.tflite`

## Define labelmap for model (default: labelmap.txt)

`-l labelmap.txt`
