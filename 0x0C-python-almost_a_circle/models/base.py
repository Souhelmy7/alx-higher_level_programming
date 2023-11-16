#!/usr/bin/python3
""" this module is about class named base"""


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this function to define instance attribute """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
