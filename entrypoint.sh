#!/bin/bash

# remove all __pycache__ directories excluding those under .venv
find . -name '__pycache__' -exec rm -rf {} \;  # force delete __pycache__

# navigate to the src directory
cd src || { echo "src directory not found!"; exit 1; }

# set default port to 8080 if APP_PORT is not provided
PORT=${APP_PORT:-8080}

# execute the main.py file with the specified port
python3 main.py --port "$PORT"
