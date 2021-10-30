#!/usr/bin/python3
""" Defining Square Class"""


class Square:
    """
    Defines a square

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square

        Args:
        size(int) = size of a square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2
            or type(value[0]) is not int or type(value[1]) is not int
            or value[0] < 0 or value[1] < 0):

            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
