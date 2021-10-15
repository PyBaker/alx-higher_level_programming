#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        print("not valid string")
        return 0
    d = {
            'I': 1,
            'V': 5,
            'X':10,
            'L': 50,
            'C': 100,
            'D': 500
    }
    total = 0
    if roman_string[0] == 'I':
        d['I'] = -1
    for letter in roman_string:
        total = total + d[letter]
    return total
