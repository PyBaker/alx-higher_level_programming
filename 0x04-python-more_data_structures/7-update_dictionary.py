#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    '''update dict with key value pair and adds new pair is does not exist'''
    keyPair = {key: value}
    return a_dictionary.update(keyPair)
