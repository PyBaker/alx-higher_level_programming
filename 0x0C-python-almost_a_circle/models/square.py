#!/usr/bin/python3
""" Module ./square.py
    Defines a square class
"""
from rectangle import Rectangle

class Square(Rectangle):
    """ Defines a Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialises Square attributes """

o = Square()
print(o)

