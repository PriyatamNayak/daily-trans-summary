
# Daily Transaction Summary

This repository contains code which generates a summary report of daily transactions in csv format






## Environment Requirements and Setup

please install python >=3.8

With Python and pip pre-installed, execute
```
cd scripts
./bootstrap_environment.sh

```
```
source virtualenv_utils.sh
activate_virtualenv
cd ..
```
to bootstrap the environment.

This will subsequently install

1. the ``virtualenv`` package
2. the virtualenv ``daily_trans_venv``
3. all required site-packages listed in ``requirements.txt`` in the previously created ``daily_trans_venv`` virtualenv



# How To Run The daily_trans_summary Tool
 Please use the below command
```


python run.py -i Input.txt -o Output.csv





```






## Running The Tests

The ``scripts`` directory also contains a Bash script for running all tests in



The script is basically a wrapper around the ` python -m unittest discover -s tests -v` command.

To start the tests execute the commands
```
cd scripts
./run_all_tests.sh
```
The script executes all tests in verbose mode and quits without any further action required.






### Summary Ouput
````
Client_Information,Product_Information,Total_Transaction_Amount
CL-1234-0002-0001,SGX-FU-NK-20100910,-52
CL-1234-0003-0001,CME-FU-N1-20100910,285
CL-1234-0003-0001,CME-FU-NK.-20100910,-215
CL-4321-0002-0001,SGX-FU-NK-20100910,46
CL-4321-0003-0001,CME-FU-N1-20100910,-79

````


## Technical Notes

### Tools Used

Implementation has been developed on a MacBook running Mac OS X 10.6.8. For Python , PyCharm 4.5.1 has been used.


### Package Overview
````
    run.py : This driver python file which will run the tool.
    requirements.txt :  This file contains all the require python pacakges
    tests : 
        This Folder contains all test cases
    daily_trans_summary : This Folder contains all the actual and transormation code
    scripts : This Folder contains some unix scripts to set virtual environments and run the test cases
    log : This Folder contains the log files
    documentation:  This Folder contains the requirement docs
    
 ````   
    
###  More Set up and installation Help and how to run the script

Windows
====================

Ensure  PYTHON >3.8is installed.

Run following commands::
````
    pip3 install virtualenv
    python -m virtualenv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
    python run.py -i Input.txt -o Output.csv

    To run test case :
    python -m unittest discover -s tests

````
OS X
====================

Ensure PYTHON >3.8  is installed::
````
    sudo pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python run.py -i Input.txt -o Output.csv
````
Alpine Linux
=====================================
````
    # setup.py -> py-setuptools
    # cryptography -> libffi-dev -> python2-dev
    # cryptography -> openssl-dev
    RUN apk add py-setuptools libffi-dev python2-dev openssl-dev
    RUN mkdir /sources/simw-top_build
    RUN cd /sources/simw-top_build \
        && cmake ../simw-top \
            -DWithHost_PCLinux64=ON \
            -DWithSMCOM_JRCP=ON \
            -DWithSMCOM_VCOM=OFF \
        && make sssapisw -j

    RUN cd /sources/simw-top/pycli/src \
        && python3 setup.py develop
        
    sudo pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python run.py -i Input.txt -o Output.csv

````
### More Usage Of Scripts

````
usage: run.py [-h] [-V] [-v VERBOSE] -i INPUT_FILE [-o OUTPUT_FILE]

This Python Scripts generates Daily Summary Report of Future Transactions done by client 1234 and 4321

options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -v VERBOSE, --verbose VERBOSE
                        default is info , 1 : warning 2: error 3: debug
  -i INPUT_FILE, --input_file INPUT_FILE
                        Path to input file ex: C:\example\Input.txt
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Path to output file C:\example\Output.csv
````

## Output CSV has the following Headers
- Client_Information
- Product_Information
- Total_Transaction_Amount



