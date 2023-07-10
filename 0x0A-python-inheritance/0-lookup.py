#!/usr/bin/python3
"""
Add attribute.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list containing the names of
        the attributes and methods of the object.
    """
    return dir(obj)
