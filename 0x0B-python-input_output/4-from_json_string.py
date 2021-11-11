#!/usr/bin/python3
""" Module ./4-from_json_string.py
    Contains:
        Function from_json_string(obj) --> convert JSON to python Dictionary
"""
import json


def from_json_string(my_str):
    """ Converts JSON to python Dictionary """
    return json.loads(my_str)
