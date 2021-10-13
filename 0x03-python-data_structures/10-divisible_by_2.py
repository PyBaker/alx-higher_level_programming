#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    result_list = my_list[:]
    for i,value in enumerate(result_list):
        if abs(value) % 2 == 0:
            result_list[i] = True
        else:
            result_list[i] = False

    return result_list

