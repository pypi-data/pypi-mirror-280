#!/bin/bash
echo "Running init_container.sh, use this script to install libraries etc."


pre-commit install

pip install -e .[dev]

git submodule init
git submodule update

pip install -e submodules/roxbot
