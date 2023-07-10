#!/usr/bin/python3
"""
Instance of the same class.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is exactly an instance
        of the specified class, False otherwise.
    """
    return type(obj) == a_class
