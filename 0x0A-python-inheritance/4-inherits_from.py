#!/usr/bin/python3
"""
This module provides a single function 'inherits_from' that
can be used to   returns True if the object is an instance of
a class that inherited (directly or indirectly) from the specified
class ;otherwise False.
"""


def inherits_from(obj, a_class):
    """
    This function returns true if the object is an instance
    of a class that inherited (directly or indirectly) from the specified
    class, otherwise return false
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
