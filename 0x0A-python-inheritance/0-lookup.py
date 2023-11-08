#!/usr/bin/python3
"""
This module provides a single function 'lookup' that
can be used to retrieve a list of attributes and methods
of any Python object.
"""


def lookup(obj):
    """
    This function returns list of available attributes and methods of an object
    """
    return dir(obj)
