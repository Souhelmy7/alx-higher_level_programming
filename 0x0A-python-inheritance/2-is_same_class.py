#!/usr/bin/python3
"""
This module provides a single function 'is_same_class' that
can be used to check if the object is exactly an instance
of the specified class
"""


def is_same_class(obj, a_class):
    """
    This function returns true if the object is exactly an instance
    of the specified class, otherwise return false
    """
    return type(obj) is a_class
