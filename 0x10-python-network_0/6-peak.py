#!/usr/bin/python3

def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    return max(list_of_integers)
