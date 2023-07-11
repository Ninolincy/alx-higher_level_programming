#!/usr/bin/python3

"""
Returns object JSON string
"""

import json


def from_json_string(my_str):
    """
    Return the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string.

    Returns:
        object: The Python data structure represented by the JSON string.

    """
    return json.loads(my_str)
