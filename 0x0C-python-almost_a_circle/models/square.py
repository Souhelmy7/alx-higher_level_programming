#!/usr/bin/python3
""" this module is about class named square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this class name square"""
    def __init__(self, size, x=0, y=0, id=None):
        """this function to define instance attribute """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this function to it returns [Square] (<id>) <x>/<y> - <size>"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """function to update the class Square"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """function returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
