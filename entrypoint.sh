#!/bin/bash

# remove all __pycache__ directories excluding those under .venv
sudo find . -name '__pycache__' -exec rm -rf {} \;  # force delete __pycache__

# set default port to 8080 if APP_PORT is not provided
PORT=${APP_PORT:-8080}

# Add current directory to PYTHONPATH
export PYTHONPATH=$(pwd):$PYTHONPATH

# execute the main.py file with the specified port
python3 src/main.py --port "$PORT"
