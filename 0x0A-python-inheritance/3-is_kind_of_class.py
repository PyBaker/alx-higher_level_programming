#!/usr/bin/python3
""" Module to check types of instances """


def is_kind_of_class(obj, a_class):
    """
    Check if object is instance o Class (a_class) directly
    or if object is inherited
    """

    return True if isinstance(obj, a_class) else False
