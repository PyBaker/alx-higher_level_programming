#!/usr/bin/python3
""" Module 5-base_geometry """


class BaseGeometry:
    """ class for base_geometry """

    def area(self):
        """ Will raise exeption when called """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validated integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Class for Rectangle shapes """

    def __init__(self, width, height):
        """ initialises Rectangle class """
        super().integer_validator("width", width)
        super().integer_validator("height", width)
        self.__width = width
        self.__height = height

    def area(self):
        """ Extends method from BaseGeometry and returns area of Rectangle """
        return self.__height * self.__width

    def __str__(self):
        """ returns name of shape and dimensions """
        return "[{:s}] {:d}\\{:d}".format(self.__class__.__name__,
                                          self.__width, self.__height)

class Square(Rectangle):
    """ Class for Square shapes """

    def __init__(self, size):
        """ initialises Square class """
        self.integer_validator("side", size)
        self.__size = size

    def area(self):
        """ Extends method from BaseGeometry and returns area of Square """
        return self.__size ** 2

    def __str__(self):
        """ returns name of shape and dimensions """
        return "[{:s}] {:d}\\{:d}".format(self.__class__.__name__,
                                          self.__size, self.__size)
