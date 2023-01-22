import logging
import os
import sys
from daily_trans_summary.util import read_fixed_width_data, dataframe_to_csv
from daily_trans_summary.constants import (Message,
                                           ProductInformation,
                                           ClientInformation,
                                           TotalTransactionAmount,
                                           CsvHeader
                                           )

__author__ = 'Priyatam Nayak'

logger = logging.getLogger(__name__)
field_names_list = [fields.name for fields in Message.fields]
group_by_fields_list = [fields.name for fields in Message.groupby_fields]
qt_long = Message.quantity_long.name
qt_short = Message.quantity_short.name


class Analysis:
    """
    This class process the input transaction file and prepare csv summary report
    parameters:
        input_file: string
           input file path
        output_file: string
            output file path
    """

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def input_feed_processing(self):
        """
        This method generates a dataframe from input file
        parameters:
             None

        :return:
           dataframe
        """
        if not os.path.exists(self.input_file):
            logger.error("The Input file path deos not exist")
            raise FileNotFoundError(f"No such file or directory: {self.input_file}")
        try:
            # Read the Input file
            logger.info(f"The input file processing is started: {self.input_file}")
            df = read_fixed_width_data(self.input_file, field_names_list=field_names_list,
                                       colspecs=[(obj.offset, obj.end) for obj in Message.fields],
                                       dtype={Message.account_number.name: object,
                                              Message.sub_account_number.name: object}
                                       )
            logger.debug(f"The dataframe creation completed")
            logger.debug(f"The dataframe transformation and aggregation  started")
            df_aggr = df.groupby(group_by_fields_list).agg({qt_long: 'sum', qt_short: 'sum'}).reset_index()
            df_aggr[TotalTransactionAmount.name] = df_aggr[qt_long] - df_aggr[qt_short]
            df_aggr[ClientInformation.name] = df_aggr[ClientInformation.value].apply(
                lambda x: '-'.join(x.dropna().astype(str)),
                axis=1
            )
            df_aggr[ProductInformation.name] = df_aggr[ProductInformation.value].apply(
                lambda x: '-'.join(x.dropna().astype(str)),
                axis=1
            )
            logger.debug(f"The dataframe transformation and aggregation  completed {df_aggr}")
            return df_aggr

        except Exception as err:
            logger.error(f"Error while attempting to process the file {err}")
            logger.critical(f"Unknown error while attempting to process file ", exc_info=True)

    def run(self):
        if os.path.isdir(self.output_file):
            if not os.path.exists(os.path.dirname(self.output_file)):
                logger.error("The Output file path is not exist")
                raise FileNotFoundError(f"No such file or directory: {self.output_file}")
        out_df = None
        try:
            out_df = self.input_feed_processing()

        except IOError:
            logger.error(f"Output File not found: {self.output_file}")
            logger.critical("File not found:", exc_info=True)
        except Exception as err:
            logger.error(f"Error while attempting to process the file {err}")
            logger.critical(f"Unknown error while attempting to process file ", exc_info=True)
        if out_df.empty:
            logger.error(f"Input file contains invalid contents or File is empty: {self.input_file}")
            raise ValueError(f"Input file contains invalid contents: {self.input_file}")
        try:
            dataframe_to_csv(out_df, CsvHeader.value, self.output_file)
        except Exception as err:
            logger.error(f"Error while attempting to process the file {err}")
            logger.critical(f"Unknown error while attempting to process file ", exc_info=True)