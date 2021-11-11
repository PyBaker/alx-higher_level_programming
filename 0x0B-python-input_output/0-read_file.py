#!/usr/bin/python3
""" Module 0-read_file

    Contains:
        Function - read_file(filename="") --> reads a text file
"""


def read_file(filename=""):
    """ Reads a file """
    with open(filename, "r") as f:
        data = f.read()
        print(data)

