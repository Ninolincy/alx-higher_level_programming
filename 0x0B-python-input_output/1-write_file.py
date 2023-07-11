#!/usr/bin/python3

"""
Write a string to a text.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)
    and return the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
