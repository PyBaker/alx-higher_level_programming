#!/usr/bin/python3
""" Module with MyList Class that which inherits list """


class MyList(list):
    """ MyList Class for Printing output """

    def print_sorted(self):
        """ Prints new list in ascending order """
        print(sorted(self))
