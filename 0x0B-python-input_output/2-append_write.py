#!/usr/bin/python3

"""
Appends a string at the end of a text.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8)
    and return the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.

    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_char_added = file.write(text)
    return num_char_added
