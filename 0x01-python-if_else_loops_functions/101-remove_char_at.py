#!/usr/bin/python3


def remove_char_at(str, n):

    newStr = ""

    for position in range(len(str)):
        if position == n:
            continue
        newStr += str[position]

    return newStr
