#!/usr/bin/python3


def no_c(my_string):
    '''Remove letter 'c' and 'C' from string'''

    dictionary = {ord(i): None for i in 'cC'}
    return(my_string.translate(dictionary))
