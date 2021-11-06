#!/usr/bin/python3
''' Module with funtions to manipulate text'''


def text_indentation(text):
    ''' Function to and new line after each occurance of "." "?" and ":"'''

    if not isinstance(text ,str):
        raise TypeError('text must be a string')


    for char in '.?:':
        text = text.replace(char, char + "\n")


    #text = text.split(sep='\n')
    #text = text.strip(' ')

    # print (' '.join([line.strip("BAZZ")] for line in text))
    print ('\n\n'.join([line.strip() for line in text.split('\n')]))




































    '''
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    '''
