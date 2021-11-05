#!/usr/bin/python3
'''
Module with funtions :
say_my_name --> prints string with first name and last name
'''


def say_my_name(first_name, last_name=""):

    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {0:s} {1:s}".format(first_name, last_name))
    else:
        raise TypeError("{:s} must be a string"
                        .format('last_name' if isinstance(first_name, str)
                                else 'first_name'))


def main():
    say_my_name(4, 'Hello')


if __name__ == "__main__":
    main()
