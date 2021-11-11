#!/usr/bin/python3
""" Module ./6-load_from_json_file.py
    Contains:
        Function load_from_json_file --> Creates python obj from JSON
"""
import json


def load_from_json_file(filename):
    """ loads and create python obj from JSON """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
