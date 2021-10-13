#!/usr/bin/python3


def max_integer(my_list=[]):

    max_num = 0
    if len(my_list) == 0:
        return None
    for i in my_list:
        max_num = i if i > max_num else max_num
    return max_num
