#!/bin/bash

source virtualenv_utils.sh
activate_virtualenv



pushd "${BASE_DIR}"

echo 'Running tests in daily trans summary'
python -m unittest discover -s tests -v



popd