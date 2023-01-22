import os
import logging

__author__ = 'Priyatam Nayak'

# DEFAULT OUTPUT FILE
DEFAULT_OUTPUT_FILE = "Output.csv"
LOG_FILE_NAME = "dailyTransSummary.log"
LOG_FILE_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log/dailyTransSummary.log")
os.makedirs(os.path.dirname(LOG_FILE_FOLDER), exist_ok=True)

# Gets or creates a logger
logger = logging.getLogger()

# set log level
logger.setLevel(logging.INFO)

# define file handler and set formatter
file_handler = logging.FileHandler(LOG_FILE_FOLDER, mode="a", encoding=None, delay=False)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

script_description = "This Python Scripts generates Daily Summary Report of Future Transactions done by client 1234 " \
                     "and 4321 "
script_version = "0.1"
