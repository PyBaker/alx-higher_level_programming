#!/usr/bin/python3
""" Module ./5-save_to_json_file.py
    Contains:
        Function save_to_json_file --> writes obj to file in JSON format
"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes python data as JSON to file """
    with open(filename, "w", ecoding="UTF-8") as f:
        json.dump(my_obj, f)
