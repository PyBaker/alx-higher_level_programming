#!/usr/bin/python3
""" Module ./8-class_to_json.py
    Returns the dictionary description with simple data structure for JSON
"""


def class_to_json(obj):
    """ Returns a dictionary description of a class"""
    return obj.__dict__
