#!/usr/bin/python3

"""
Returns dic discription.
"""


def class_to_json(obj):
    """
    Return the dictionary description with a simple
    data structure for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary description of the object.

    """
    return obj.__dict__
