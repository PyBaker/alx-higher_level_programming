#!/usr/bin/python3
""" Module ./rectangle.py
    Initialises a Rectangle Class (child class of Base Class)
"""
from models.base import Base


class Rectangle(Base):
    """ Defines a Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialises Rectangle Class with gived fields """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        print("height is {}".format(value))
        if type(value) is not int:
            raise typeerror("height must be an integer")
        elif value <= 0:
            raise valueerror("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise typeerror("x must be an integer")
        if x < 0:
            raise valueerror("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

