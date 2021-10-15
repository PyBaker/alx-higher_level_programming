#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    numPrinted = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            numPrinted += 1
    except IndexError:
        pass
    finally:
        print()
    return numPrinted
