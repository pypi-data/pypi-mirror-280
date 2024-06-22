# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved.

"""
Module for methods shared between all XLSX-type readers.
"""

import logging
import pathlib
from typing import Any, Dict, List
import pandas
import numpy


class XLSXReaderError(Exception):
    """
    Error indicating problems in reading an XLSX file.
    """

class XLSXReaderEmptyStringError(XLSXReaderError):
    """
    Error caused by encountering an emtpy string while content is required.
    """

class XLSXReaderInvalidValue(XLSXReaderError):
    """
    Error caused by using an invalid value for a parameter (e.g., using a list where only strings are allowed).
    """


PRAGMA_FOR_EXPRESSION = '#'
KEYWORDS_DEFAULT = ["NONE", ""]
KEYWORDS_NONE = ["NONE"]
KEYWORD_COMMENTS = "COMMENTS"

def read(file_path: pathlib.Path) -> Dict[str, pandas.DataFrame]:
    """
    Read the XLSX files at the location given by the parameter and return its contents as a dictionary of Pandas
    dataframes. Keys of the dictionaries will be set to worksheet names.

    Args:
        file_path
            Location of the xlsx-style file.

    Returns
        A dictionary of the Pandas dataframes created from the given file.
    """
    data = pandas.read_excel(file_path,
                             sheet_name=None,
                             engine='openpyxl',
                             keep_default_na=False,
                             dtype=str)

    dictionary = {}
    for key in data.keys():
        dictionary[key] = data[key].to_dict('index')
    return dictionary

def clean_boolean_cell_else_raise(cell_content: str, exception_message_hint: str = "") -> bool:
    """
    Extracts a unique boolean value from a string, ingnoring unnecessary characters.
    Args: 
        entry_str (str): String which is to be validated and cleaned.
        exception_message_hint (str): Hint about where the string comes from to augment the exception message.
    
    Returns:
        float: The float submitted by the user.

    Raises:
        XLSXReaderInvalidValue: if the user attempts to pass something else than an integer. 
        XLSXReaderEmptyStringError: if the output string is empty.
    """
    cleaned_cell_content = clean_str(cell_content, exception_message_hint)
    accepted_true_strings = ["TRUE", "1", "YES"]

    return cleaned_cell_content in accepted_true_strings


def clean_int_cell_else_raise(cell_content: str, exception_message_hint: str = "") -> int:
    """
    Extracts a unique number from a string, ingnoring unnecessary characters. Checks if the contents of the cleaned
    {entry_str} contain a list. If any additional restictions are to be put on fields containing strictly individual
    integer, they can be added here.

    Args: 
        entry_str (str): String which is to be validated and cleaned.
        exception_message_hint (str): Hint about where the string comes from to augment the exception message.
    
    Returns:
        int: The integer submitted by the user.

    Raises:
        XLSXReaderInvalidValue: if the user attempts to pass something else than an integer. 
        XLSXReaderEmptyStringError: if the output string is empty.
    """
    cleaned_cell_content = clean_str(cell_content, exception_message_hint)

    try:
        return int(cleaned_cell_content)
    except ValueError as exc:
        message_exception = f"The string {cleaned_cell_content} does not contain an individual integer." \
                            f"Additional information about this error: {exception_message_hint}"
        logging.exception(message_exception)
        raise XLSXReaderInvalidValue(message_exception) from exc

def clean_float_cell_else_raise(cell_content: str, exception_message_hint: str = "") -> float:
    """
    Extracts a unique number from a string, ingnoring unnecessary characters. Checks if the contents of the cleaned
    {entry_str} contain a list. If any additional restictions are to be put on fields containing strictly individual
    float, they can be added here.

    Args: 
        entry_str (str): String which is to be validated and cleaned.
        exception_message_hint (str): Hint about where the string comes from to augment the exception message.
    
    Returns:
        float: The float submitted by the user.

    Raises:
        XLSXReaderInvalidValue: if the user attempts to pass something else than an integer. 
        XLSXReaderEmptyStringError: if the output string is empty.
    """
    cleaned_cell_content = clean_str(cell_content, exception_message_hint)

    try:
        return float(cleaned_cell_content)
    except ValueError as exc:
        message_exception = f"The string {cleaned_cell_content} does not contain an individual floating point" \
                            f"number. Additional information about this error: {exception_message_hint}"
        logging.exception(message_exception)
        raise XLSXReaderInvalidValue(message_exception) from exc

def clean_str_cell_else_raise(entry_str: str, exception_message_hint: str = "") -> str:
    """
    Extracts a unique word within a string, removing unnecessary characters and forcing to uppercase. Tests the 
    contents of the cleaned {entry_str} contains a list. If any additional restictions are to be put on fields
    containing strictly individual values (as opposed to lists), they can be added here.

    Args: 
        entry_str (str): String which is to be validated and cleaned.
        exception_message_hint (str): Hint about where the string comes from to augment the exception message.
    
    Returns:
        str: The string without invalid characters.

    Raises:
        XLSXReaderInvalidValue: if the input is a list. 
        XLSXReaderEmptyStringError: if the output string is empty.
    """
    ret = clean_str(entry_str, exception_message_hint)

    if (ret[0] == "[" and ret[-1] == "]") or ',' in ret:
        message_exception = f"The string {entry_str} is a list. Lists are not allowed in this parameter." \
                            f"Additional information about this error: {exception_message_hint}"
        logging.exception(message_exception)
        raise XLSXReaderInvalidValue(message_exception)
    return ret

def clean_input_string(entry_string: str) -> str:
    """
    Applying basic transformations to input cells; removing spaces and quotation marks. It also transforms the text to
    uppercase. 

    Args:
        entry_string:
            String to which the modifications will be applied.
    
    Returns:
        entry_string after applying the simple transformations unifying the user inputs.
    """
    return entry_string.replace(" ", "").replace("'", "").replace('"', '').replace('“', '').replace('”', '').upper()

def clean_str(entry_str: str, exception_message_hint: str = "") -> str:
    """
    Extracts a unique word within a string, removing spaces, quote marks and making it uppercase.

    Args:
        entry_str (str): Input string.
        exception_message_hint (str): Hint about where the string comes from to augment the exception message.
    
    Returns:
        str: The string without invalid characters.

    Raises:
        XLSXReaderEmptyStringError: if the output string is empty.
    """
    ret: str = clean_input_string(entry_str)
    if ret == "":
        message_exception = f"Empty string in one cell, here is an exception_message_hint," \
                            f"maybe: {exception_message_hint}"
        logging.exception(message_exception)
        raise XLSXReaderEmptyStringError(message_exception)
    return ret

def clean_list_cell(cell_entry_str: str, exception_message_hint: str = "") -> List[Any]:
    """
    Extracts elements from a given list in the format '[1., 2., 3.]'
    :param cell_entry_str is a string representing either a list of float or a list of string.
    :param exception_message_hint: hint about where does the string comes from in order to
    print a debug information
    """

    # if the string start with a '#', then it's some expression to evaluate
    if cell_entry_str[0] == PRAGMA_FOR_EXPRESSION:
        output_list = eval(cell_entry_str[1:])
        if isinstance(output_list,(numpy.ndarray,range)):
            output_list=list(output_list)
        if not isinstance(output_list,list):
            message_exception = f"A string containing {PRAGMA_FOR_EXPRESSION} as " \
                                f"first character has been evaluated to extract a list out " \
                                f"of it but the attempt failed. The content of the string " \
                                f"is {cell_entry_str}, the variable evaluated is " \
                                f"{output_list} of type {type(output_list)}"
            logging.exception(message_exception)
            raise XLSXReaderError(message_exception)

    else:
        # This function has to handle manually typed lists
        #
        # Example lists: "1", "[1, 2, 3, 4]", "[1], [2], [3]", "graph, summary", "[“graph”, “summary”]",
        # "[[1, 2], [3, 4]]", "[1, 2, 3], [4, 5, 6]"
        #

        cell_entry_str = clean_str(cell_entry_str, exception_message_hint + "- cleaning string of a list")
        def parse(string):
            lists_pointers = [[]]
            word_buffer = []

            def start_list():
                new_list = []
                lists_pointers[-1].append(new_list)
                lists_pointers.append(new_list)

            def end_list():
                if word_buffer:
                    new_element()
                lists_pointers.pop()

            def new_element():
                if not lists_pointers[0]:
                    start_list()
                if word_buffer:
                    element = "".join(word_buffer)
                    try:
                        element = float(element)
                    except ValueError:
                        pass
                    lists_pointers[-1].append(element)
                    word_buffer.clear()

            actions = {
                '[': start_list,
                ']': end_list,
                ',': new_element
            }

            for char in string:
                actions.get(char, lambda: word_buffer.append(char))()

            if word_buffer:
                new_element()
            return lists_pointers[0][0] if len(lists_pointers[0]) == 1 else lists_pointers[0]

        output_list = parse(cell_entry_str)
    return output_list

def transform_str_of_list_in_list(str_in) -> List[Any]:
    """
    Test to check if a string contains a list
    """
    if str_in[0] == "[" and str_in[-1] == "]":
        return clean_list_cell(str_in)
    return str_in

def get_cell_text(row, column_name: str = KEYWORD_COMMENTS) -> str:
    """Method to read text from a cell
    
    This function is supposed to be used when it does not matter what is the content of the read cell: it can be a
    number, a string, a lower or uppercase paragrah. Useful, e.g., for comments cells, which are not supposed to be 
    parsed or validated in any specific ways. The function does not throw an error when a given column does not exist.
    By default it attempts to read the comments column.

    Args:
        row
            The input row received from the reader.
        column_name
            The name of the column to be read.
 
    Returns: 
        A string which contains whatever text is placed in the input cell. Might be empty.
    """
    text = ""
    try:
        text = row[column_name]
    except KeyError:
        pass
    return text

def read_cell_str_with_default(cell_content, exception_message_hint, default = "") -> str:
    """It's a shorthand function for returning a default value if the input cell is empty (as defined by the parameter)
    or parsing a string from that cell"""
    cell_content = cell_content.upper()
    return default if cell_content in KEYWORDS_DEFAULT \
        else clean_str_cell_else_raise(cell_content, exception_message_hint)

def read_cell_list_with_default(cell_content, exception_message_hint, default = None):
    """It's a shorthand function for returning a default value if the input cell is empty (as defined by the parameter)
    or parsing a list from that cell"""
    default = [] if default is None else default
    cell_content = cell_content.upper()
    return default if cell_content in KEYWORDS_DEFAULT else clean_list_cell(cell_content, exception_message_hint)
