#!/usr/bin/python3
'''This module contains functions to print square shapes'''


def print_square(size):
    ''' Prints a square with size and the lenght of one side'''

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    print('\n'.join(['#' * size] * size))
