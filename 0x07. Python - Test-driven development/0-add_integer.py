#!/usr/bin/python3
'''
Define an integer addition function
Float are typecast to int before addidtion
'''


def add_integer(a, b=98):
    """Return the integer addition of a and b
    Raises: TypeError: If a or b is a not an integer and not a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
