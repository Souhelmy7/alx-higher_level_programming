#!/usr/bin/python3
""" this module is about class named base"""
import json
import csv
import os.path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
