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
        # print("i am size {} and i'm varible {}".format(size, self.__size))

    @property
    def size(self):
        # print("this is the getter")
        return self.__size

    @size.setter
    def size(self, value):
        # print ("this is th value {}".format(value))

        if type(value) is not int:
            # print("Hello")
            raise TypeError("size must be an integer")
        elif value < 0:
            # print("World")
            raise ValueError("size must be >= 0")
        else:
            # print("i'm done setting value {} to __size {}"
            # .format(value, self.__size))
            self.__size = value

    def area(self):
        return (self.__size) ** 2
