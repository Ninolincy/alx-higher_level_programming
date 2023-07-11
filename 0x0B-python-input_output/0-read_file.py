#!/usr/bin/python3

"""
Reads and print text.
"""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print its content to stdout.

    Args:
        filename (str): The name of the file.

    Returns:
        None

    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
