#!/usr/bin/python3
""" Module ./base.py
    Initialises a Base Class
"""


class Base:
    """ Defines a Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            __nb_objects += 1
            self.id = __nb_objects
