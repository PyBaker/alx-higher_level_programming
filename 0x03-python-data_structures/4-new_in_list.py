#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    copyOfList = my_list[:]
    if idx < 0:
        return None
    elif idx > len(copyOfList):
        return None
    else:
        copyOfList[idx] = element
        return(copyOfList)
