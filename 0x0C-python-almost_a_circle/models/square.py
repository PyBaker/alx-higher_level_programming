#!/usr/bin/python3
""" Module ./square.py
    Defines a square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialises Square attributes """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return custom string """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.__class__.__name__, self.id,
                    self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ Updates the Square

        Args:
            *args(ints): New attribute values.
            1st argument --> id attribute
            2nd argument --> size attribute
            3rd argument --> x attribute
            4th argument --> y attribute

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
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
            break

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.sizej, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, value):
        """ set size """
        self.width = self.height = value
