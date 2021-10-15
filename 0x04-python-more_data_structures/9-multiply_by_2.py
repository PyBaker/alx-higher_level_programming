#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    newDict = {}
    for key,value in a_dictionary.items():
        keyPair = {key: int(value) * 2}
        newDict.update(keyPair)
    return newDict

