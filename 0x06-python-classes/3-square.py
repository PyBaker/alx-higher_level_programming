#!/usr/bin/python3
""" Defining Square Class"""


class Square:
    """
    Defines a square

    """
    def area(self):
        return self.__size ** 2

    def __init__(self, size=0):
        """
        Initialize a square

        Args:
        size(int) = size of a square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
