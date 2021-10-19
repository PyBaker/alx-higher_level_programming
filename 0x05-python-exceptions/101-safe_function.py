#!/usr/bin/python3


def safe_function(fct, *args):
    ''' catches errors when function call has errors'''
    res = None
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e))
    finally:
        pass
    return res
