#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    #incase tuples do not match in size(only 0,1,2 number of elements

    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    return(tuple(map(lambda i, j: i + j, tuple_a[:2], tuple_b[:2])))
