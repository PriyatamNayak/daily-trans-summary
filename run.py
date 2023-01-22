#!/usr/bin/python
import os
import sys
import logging
from daily_trans_summary.setting import DEFAULT_OUTPUT_FILE, script_version, script_description
from daily_trans_summary.util import make_argsparse, set_log_level_from_verbose
from daily_trans_summary.analyze import Analysis

logger = logging.getLogger(__name__)


def main(arguments):
    print("The Script Started")
    try:
        logger.info("The transaction summary  report scripts started")
        input_file_name = arguments.input_file
        output_file_name = arguments.output_file
        logger.info(f"The Input parameters are {arguments}")
        print(f"The Input parameters are {arguments}")
        if not os.path.exists(input_file_name):
            logger.error("The Output file path deos not exist")
            raise FileNotFoundError(f"No such file or directory: {input_file_name}")
        if os.stat(input_file_name).st_size < 0:
            logger.error("The Input  file  is empty")
            raise ValueError("The input file can not be empty")
        if os.path.isdir(output_file_name):
            if not os.path.exists(os.path.dirname(output_file_name)):
                logger.error("The Output file path is not exist")
                raise FileNotFoundError(f"No such file or directory: {output_file_name}")

        logger.info(f"The input file processing is started")
        logger.debug(f"The Input File path: {input_file_name}")
        Analysis(input_file_name, output_file_name).run()
        logger.info("The transaction summary  report scripts Completed")
        print("The Script Completed")
    except Exception as err:
        logger.error(f"The transaction summary  report scripts completed with errors {err}")
        logger.critical("unknown error while attempting to read file length", exc_info=True)
        print("The Script ended with some errors")


if __name__ == '__main__':
    logger.debug(f" The input parameters: {sys.argv[2:]}")
    ap = make_argsparse(DEFAULT_OUTPUT_FILE, script_version, description=script_description)
    args = ap.parse_args()
    set_log_level_from_verbose(logger, args)
    main(args)
