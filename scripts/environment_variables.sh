#!/bin/bash

# Stop on all errors
set -e


BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/../"
VIRTUALENV_DIR="${BASE_DIR}/../virtualenvs"
VIRTUALENV_NAME="daily_trans_venv"
VIRTUALENV_LOCATION="${VIRTUALENV_DIR}/${VIRTUALENV_NAME}"
