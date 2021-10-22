#!/usr/bin/python3
""" Defining Square Class"""


class Square:
    """
    Defines a square

    """
    def __init__(self, size=0):
        """
        Initialize a square

        Args:
        size(int) = size of a square
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size)**2
