#!/usr/bin/python3
''' This module tests adds two numbers and casts floats to int'''

def add_integer(a, b=98):
    ''' return sum of two numbers '''
    if type(a) is not int:
        raise(TypeError("a must be an integer")
    elif type(b) is not int:
        raise(TypeError("b must be an integer")
    elif type(a) is float:
        a = int(a)
    elif type(b) is float
        b = int(b)
    else:
        return (a + b)
