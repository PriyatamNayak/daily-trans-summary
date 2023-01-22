import os
import unittest
from pathlib import Path
import pandas as pd
from daily_trans_summary.analyze import Analysis
from daily_trans_summary.util import make_argsparse, dataframe_to_csv, read_fixed_width_data

__author__ = 'Priyatam Nayak'

TEST_CASE_DIR = os.path.dirname(os.path.abspath(__file__))


def casepath(relative_path):
    return os.path.join(TEST_CASE_DIR, relative_path)


class TestAnalyze(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.input_valid_file = Path(casepath("data/Input.txt"))
        cls.input_invalid_file = Path(casepath("data/input_invalid.txt"))
        cls.input_empty_file = Path(casepath("data/input_empty.txt"))
        cls.output_file = Path(casepath("data/Output.csv"))
        cls.df_expected = pd.DataFrame({'Total_Transaction_Amount': [-52, 285, -215, 46, -79],
                                        'Product_Information': ['SGX-FU-NK-20100910', 'CME-FU-N1-20100910',
                                                                'CME-FU-NK.-20100910', 'SGX-FU-NK-20100910',
                                                                'CME-FU-N1-20100910'
                                                                ],
                                        'Client_Information':
                                            ['CL-1234-0002-0001', 'CL-1234-0003-0001', 'CL-1234-0003-0001',
                                             'CL-4321-0002-0001',
                                             'CL-4321-0003-0001']

                                        })

    def setUp(self) -> None:
        self.obj = Analysis(self.input_valid_file, self.output_file)

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_input_feed_processing(self):
        df_actual = self.obj.input_feed_processing()
        self.assertFalse(df_actual.empty)
        self.assertEqual(True,
                         self.df_expected['Total_Transaction_Amount'].equals(df_actual['Total_Transaction_Amount']))
        self.assertEqual(True, self.df_expected['Product_Information'].equals(df_actual['Product_Information']))
        self.assertEqual(True, self.df_expected['Client_Information'].equals(df_actual['Client_Information']))

    def test_input_feed_processing_error(self):
        self.obj_err = Analysis("input5.txt", self.output_file)
        with self.assertRaises(Exception) as context:
            self.obj_err.input_feed_processing()
        self.assertTrue('No such file or directory:' in str(context.exception))

    def test_input_feed_processing_with_invalid_file(self):
        self.obj = Analysis(self.input_invalid_file, self.output_file)
        with self.assertRaises(Exception) as context:
            self.obj.run()
        self.assertTrue('Input file contains invalid contents' in str(context.exception))

    def test_input_feed_processing_with_empty_file(self):
        self.obj = Analysis(self.input_empty_file, self.output_file)
        with self.assertRaises(Exception) as context:
            self.obj.run()
        self.assertTrue('Input file contains invalid contents' in str(context.exception))


class TestParser(unittest.TestCase):
    def setUp(self):
        self.output_file = Path(casepath("data/Output.csv"))
        self.parser = make_argsparse(self.output_file, version="0.1", description=None)

    def test_input(self):
        parser = self.parser.parse_args(['-i', "test.txt"])
        self.assertEqual(parser.input_file, 'test.txt')

    def test_output(self):
        parser = self.parser.parse_args(['-i', 'test.txt', '-o', "output.txt"])
        self.assertEqual(parser.output_file, 'output.txt')

    def test_verbose(self):
        parser = self.parser.parse_args(['-i', 'test.txt', '-v', "3"])
        self.assertEqual(parser.verbose, '3')


class TestUtil(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.input_file = Path(casepath("data/Input.txt"))
        cls.output_file = Path(casepath("data/Output.csv"))
        cls.df = pd.DataFrame({'Total_Transaction_Amount': [-52, 285, -215, 46, -79]})

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_read_fixed_width_data(self):
        df = read_fixed_width_data(self.input_file, ['test1', 'test2', 'test3'], [(3, 7), (8, 9), (10, 20)])
        self.assertFalse(df.empty)

    def test_dataframe_to_csv(self):
        dataframe_to_csv(self.df, ["Total_Transaction_Amount"], self.output_file)
        self.assertTrue(os.path.exists(self.output_file))
