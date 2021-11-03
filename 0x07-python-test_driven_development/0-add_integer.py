#!/usr/bin/python3
''' This module tests adds two numbers and casts floats to int'''


def add_integer(a, b=98):
    ''' return sum of two numbers '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
