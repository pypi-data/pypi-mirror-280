# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved.

"""
Module for testing functions of the XLSX Reader class.
"""

import unittest

from availsim4core.src.reader.xlsx import xlsx_utils

class test_XlsxReader(unittest.TestCase):
    """
    This class tests utility functions used to read and clean strings read from the XLSX files.
    """

    def test_clean_str_cell_else_raise(self):
        """
        Checking if the string cleaning works properly by removing brackets, spaces and making all letters uppercase
        """
        test_cases = ["[1, 2, 3]", "[“1.“, “2.“, “3.“]", "[\"aBa\", \"CCC\", \"tte\"]"]
        test_answers = ["[1,2,3]", "[1.,2.,3.]", "[ABA,CCC,TTE]"]
        for question, answer in zip(test_cases, test_answers):
            self.assertEqual(xlsx_utils.clean_str(question, ""), answer)

    def test_clean_str_cell_else_raise_empty(self):
        """
        Ensuring that the funtion cleaning string raises an exception when provided empty string
        """
        self.assertRaises(xlsx_utils.XLSXReaderEmptyStringError, xlsx_utils.clean_str_cell_else_raise, "")

    def test_clean_list_cell(self):
        """
        Tests of the function extracting elements from lists
        """
        test_case_answer_tuples = [("[1]", [1.0]),
                                   ("8", [8.0]),
                                   ("11, 22, 33, 44", [11.0, 22.0, 33.0, 44.0]),
                                   ("[10, 20, 30, 40]", [10.0, 20.0, 30.0, 40.0]),
                                   ("[graph, summary, rca]", ["GRAPH", "SUMMARY", "RCA"]),
                                   ("[[1.], [2.], [3.]]", [[1.0], [2.0], [3.0]]),
                                   ("[4], [5], [6]", [[4.0], [5.0], [6.0]]),
                                   ("[[1., 9.], [2., 8.], [3., 7.]]", [[1.0, 9.0], [2.0, 8.0], [3.0, 7.0]]),
                                   ]
        for question, answer in test_case_answer_tuples:
            self.assertEqual(xlsx_utils.clean_list_cell(question), answer)
