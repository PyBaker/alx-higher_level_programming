#!/usr/bin/python3


def uppercase():

    for i in range(122, 96, -2):
        print("{}{}".format(chr(i), chr(i-33)), end='')
