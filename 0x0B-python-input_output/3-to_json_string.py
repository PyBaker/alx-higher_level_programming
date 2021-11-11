#!/usr/bin/python3
""" Module ./3-to_json_string.py
    Contains:
        Function to_json_string(obj) --> convert obj to json string
"""
import json


def to_json_string(my_obj):
    """ Converts object to JSON string """
    return json.dumps(my_obj)
