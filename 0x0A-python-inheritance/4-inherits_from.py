#!/usr/bin/python3
""" Module to check types of instances """


def inherits_from(obj, a_class):
    """
    Check if object is instance a Class (a_class) directly
    or if object is inherited
    """

    return True if type(obj) is not a_class and \
        issubclass(type(obj), a_class) else False
