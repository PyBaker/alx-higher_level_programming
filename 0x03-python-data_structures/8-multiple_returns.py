#!/usr/bin/python3


def multiple_returns(sentence):
    '''return tuple of length of string and first character in string'''

    if not sentence:
        return((len(sentence),None))
    return((len(sentence),sentence[0]))
