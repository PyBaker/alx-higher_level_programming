#!/usr/bin/python3
""" Module ./square.py
    Defines a square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialises Square attributes """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return custom string """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.__class__.__name__, self.id,
                    self.x, self.y, self.size)

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, value):
        """ set size """
        self.__width = self.__height = value
