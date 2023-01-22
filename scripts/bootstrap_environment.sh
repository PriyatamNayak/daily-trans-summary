#!/bin/bash

source environment_variables.sh

echo "Step 1: Installing 'virtualenv'..."

pip install virtualenv || pip3 install virtualenv
echo "...done"


echo "Step 2: Creating the virtualenv for 'daily_trans_summary'..."
mkdir -p "${VIRTUALENV_DIR}"
pushd "${VIRTUALENV_DIR}"
virtualenv "${VIRTUALENV_NAME}"
popd
echo "...done"


echo "Step 3: Installing all site-packages in the 'daily_trans_summary' virtualenv..."
source "${VIRTUALENV_LOCATION}/bin/activate"



pip install -r "${BASE_DIR}/requirements.txt" || pip3 install -r "${BASE_DIR}/requirements.txt"

echo "...done"
echo "All Steps completed successfully."
