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
        self.__size = size

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
        return (self.__size) ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            ''' making a 2-dimenstional array is better as this method is a
            shorter way to display a shape (rectangle or square
            print('\n'.join([''.join(['#' for element in range(rows)])
                                                for col in range(column)]))
            row = length
            column = width

            therefore row and column must be set to self.__size
            '''
            print('\n'.join(['#' * self.__size] * self.__size))
