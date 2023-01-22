"""
This module contains all the util methods

"""

import os
import logging
import argparse
import pdb

import pandas as pd

__author__ = 'Priyatam Nayak'

logger = logging.getLogger(__name__)


def read_fixed_width_data(filepath, field_names_list, colspecs, dtype=None, converters=None):
    """
    Read a table of fixed-width formatted lines into DataFrame
    
    Parameters:
        filepath: path object, or file-like object
        String, path object (implementing os.PathLike[str]), or file-like object implementing a text read() function.
        The string could be a URL. Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is expected.
        A local file could be: file://localhost/path/to/table.csv.

        colspecs: list of tuple (int, int) or ‘infer’. optional
                    A list of tuples giving the extents of the fixed-width fields of each line as half-open
                    intervals (i.e., [from, to[ ). String value ‘infer’ can be used to instruct the parser to try
                    detecting the column specifications from the first 100 rows of the data which are not
                    being skipped via skiprows (default=’infer’).
        field_names_list: list 
                    column names in list format

        dtype : dict, optional
            example :  column labels  transformation data type
        converters: dict, optional
                        Keys can either be integers or column labels.
         

    Returns: pandas data frame
        DataFrame

            """
    try:
        df = pd.read_fwf(filepath, names=field_names_list,
                         colspecs=colspecs, dtype=dtype, converters=converters

                         )
        return df
    except Exception as err:
        logger.error(f"Error: Occurred when try to read the input file {err}")
        logger.critical(f"Error: Occurred when try to read the input file", exc_info=True)


def dataframe_to_csv(data_frame, csv_header_list, output_file_name, index=False):
    """
    This will prepare a csv file from pandas dataframe.

    Parameters:
            data_frame:  Pandas data frame
                 Pandas dataframe
            csv_header_list:  list
                Column Names in list format
            output_file_name:  String
                Output File Name Path
            index: boolean
                 True or False : to keep dataframe indexes in output csv or not

    Returns:
        None

    """
    if not all([csv_header_list, output_file_name, not data_frame.empty]):
        raise ValueError("Please check the inputs, inputs can not be empty ")

    try:
        data_frame[csv_header_list].to_csv(output_file_name, index=index)
    except Exception as err:
        logger.error(f"Error: Occurred when trying to convert the dataframe to csv {err}")
        logger.critical(f"Error: Occurred when trying to convert the dataframe to csv", exc_info=True)


def make_argsparse(default_output_file, version, description):
    """
        This will prepare a csv file from pandas dataframe.

        Parameters:
                default_output_file:  string
                     file path
                version:  str
                    program version
                description:  String
                     Description about the program

        Returns:
            args object

        """
    ap = argparse.ArgumentParser(fromfile_prefix_chars='@',
                                 description=description)
    ap.add_argument('-V', '--version', action='version', version='%(prog)s ' + version)
    ap.add_argument('-v', '--verbose', default='', help="default is info , 1 : warning 2: error 3: debug")
    ap.add_argument("-i", "--input_file", required=True,
                    help="Path to input file ex: C:\example\Input.txt")
    ap.add_argument("-o", "--output_file", default=os.path.join(os.getcwd(), default_output_file),
                    help="Path to output file C:\example\Output.csv")
    return ap


def set_log_level_from_verbose(logger, arguments):
    """
      This will set the logging levels
      Parameters:
                logger:  logger obj
                     file path
                arguments:  argparse object

        Returns:
            None


    """
    ver = arguments.verbose
    if ver == '':
        logger.setLevel('INFO')
    elif ver == "1":
        logger.setLevel('WARNING')
    elif ver == "2":
        logger.setLevel('ERROR')
    elif ver >= "3":
        logger.setLevel('DEBUG')
    else:
        logger.critical("UNEXPLAINED NEGATIVE COUNT!")
