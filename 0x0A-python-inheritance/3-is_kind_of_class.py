#!/usr/bin/python3
"""
This module provides a single function 'is_same_class' that
can be used to  returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns true if the object is  an instance
    or if the object is an instance of a class that inherited from,
    the specified class, otherwise return false
    """
    return isinstance(obj, a_class)
