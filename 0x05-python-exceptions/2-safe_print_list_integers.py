#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except TypeError as te:
            #print("Pano pa {}".format(te))
            pass
        except ValueError as ve:
            #print("Pano pa two {}".format(ve))
            pass
        except IndexError as ve:
            #print("Pano pa three {}".format(ve))
            pass
    print()
    return count
