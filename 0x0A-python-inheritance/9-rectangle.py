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
    """ subclass of BaseGeometry """

    def __init__(self, width, height):
        """ initialises Rectangle class """
        super().integer_validator("width", width)
        super().integer_validator("height", width)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculate the area of Rectangle """
        return self.__height * self.__width

    def __str__(self):
        return "[{}] {}\{}".format(self.__class__.__name__, self.__width, self.__height)


