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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ returns area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints rectangle with '#' symbol """
        print("\n".join(["#" * self.__width] * self.__height))

        # return ("[Rectangle] ({}) {}/{} - {}/{}"
        #        .format(self.id, self.__x,
        #                                self.__y, self.__width, self.__height))
        # self.__class__.__name__,

    def __str__(self):
        """ overrides __str__ magic method to custom text """
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d} \
                ".format(self.id,
                         self.__x, self.__y, self.__width, self.height))

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
