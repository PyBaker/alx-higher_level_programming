#!/usr/bin/python3
""" Module with functions that compare Objects """


def is_same_class(obj, a_class):
    """ Checks if object (obj) is and instance of Class (class) """

    return True if type(obj) == a_class else False
