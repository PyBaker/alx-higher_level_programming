#!/usr/bin/python3


def uppercase():

    for i in range(ord('z'), ord('a')-1, -1):
        print("{}".format(chr(i) if i % 2 == 0 else chr(i-32)), end='')
