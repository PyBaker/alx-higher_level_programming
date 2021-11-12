#!/usr/bin/python3
""" Module with functions:
        pascal_triangle --> returns a list of lists of integers
                                representing pascal triangle of given number
"""


def pascal_triangle(n):
    """ returns 2d list of integers representing pascal triangle """
    array_of_lists = []
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        triangle.append([a+b for a, b
                         in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
