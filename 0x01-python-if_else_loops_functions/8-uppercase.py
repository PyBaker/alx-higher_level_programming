#!/usr/bin/python3


def uppercase(str):

    newStr = ""

    for letter in str:
        if ord(letter) > 96 and ord(letter) < 122:
            newStr += ord(letter-32)
        else:
            newStr += ord(letter)

    print(newStr)
