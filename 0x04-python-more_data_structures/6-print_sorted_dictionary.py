#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return a_dictionary
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary[i]))
    return a_dictionary
