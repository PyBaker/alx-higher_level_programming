#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    ''' catches errors when function call has errors'''
    res = None
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        pass
    return res
