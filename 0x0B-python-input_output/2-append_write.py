#!/usr/bin/python3
""" Modlule 2-append_write
    Contains:
        Function append_write(filename="", text="") --> appends to file
"""


def append_write(filename="", text=""):
    """ Appends text to file """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return(f.write(text))
