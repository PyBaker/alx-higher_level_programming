#!/usr/bin/python3

for left in range(10):
    for right in range((left+1), 10):
        if (left != 8) or (right != 9):
            print("{}{}, ".format(left, right), end="")
        else:
            print("{}{}".format(left, right))
