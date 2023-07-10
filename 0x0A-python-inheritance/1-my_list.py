#!/usr/bin/python3
"""
MyList class.
"""


class MyList:
    """
    Custom list class that allows appending
    elements and printing the list in sorted order.
    """

    def __init__(self):
        """Initialize an empty list."""
        self._list = []

    def append(self, value):
        """Append an element to the list."""
        self._list.append(value)

    def print_sorted(self):
        """Print the list in sorted order."""
        sorted_list = sorted(self._list)
        print(sorted_list)

    def __str__(self):
        """String representation of the list."""
        return str(self._list)
