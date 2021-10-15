#!/usr/bin/python3


def search_replace(my_list, search, replace):
    ''' replace element of list with a defined replacement'''

    copyOfList=[]
    for k,v in enumerate(my_list):
        if v == search:
            my_list[k] = replace
            copyOfList.append(v)
            continue
        copyOfList.append(v)
    return copyOfList

