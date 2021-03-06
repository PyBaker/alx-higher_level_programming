#!/usr/bin/python3
""" Module 10-Square
    Contains a class Square with is a subclass of Rectangle
    Order:
        BaseGeometry --> Rectangle --> Square
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Class for Square shapes """

    def __init__(self, size):
        """ initialises Square class """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
