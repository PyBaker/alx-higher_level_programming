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
        y_coordinates = "\n" * self.__y
        x_cordinates = " " * self.__x

        shape = "\n".join([x_cordinates + "#" * self.__width] * self.__height)
        # This
        print(y_coordinates, end="")
        print(shape)

    def update(self, *args, **kwargs):
        """ Updates the Rectangle

        Args:
            *args(ints): New attribute values.
            1st argument --> id attribute
            2nd argument --> width attribute
            3rd argument --> height attribute
            4th argument --> x attribute
            5th argument --> y attribute

            kwargs(dict)
        """
        if len(args) != 0:
            for index, arg in enumerate(args):
                if index == 0:
                    if arg is None:
                        self.__init__(self.width, self.heigh, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.heigh, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns dictionary representation of Rectangle """
        my_dict = {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
        return my_dict

    def __str__(self):
        """ overrides __str__ magic method to custom text """
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}"
                .format(self.__class__.__name__, self.id,
                        self.__x, self.__y, self.__width, self.height))

    """ Getter and Setter for width """
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

    """ Getter and Setter for height """
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

    """ Getter and Setter for x """
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

    """ Getter and Setter for y """
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
