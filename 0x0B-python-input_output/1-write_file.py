#!/usr/bin/python3
""" Module 1-write_file:
    Contains:
        Function write_file() --> writes a string to a text file
"""


def write_file(filename="", text=""):
    """ Writes a string to a text file """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return(f.write(text))
