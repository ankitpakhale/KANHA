#!/bin/bash

# remove all __pycache__ directories excluding those under .venv
find . -type d -name "__pycache__" -not -path "./.venv/*" -exec rm -r {} \;

# navigate to the src directory
cd src || { echo "src directory not found!"; exit 1; }

# execute the main.py file
python3 main.py
