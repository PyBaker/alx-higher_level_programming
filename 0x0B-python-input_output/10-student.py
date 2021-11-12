#!/usr/bin/python3
""" Module ./10-student.py
    Defines a Student class with fields and methods
"""


class Student:
    """ Defines a student class """

    def __init__(self, first_name, last_name, age):
        """ initiallises student attributes

            Args:
                first_name (str): The first name of the student.
                last_name (str): The last name of the student.
                age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns dictionary representation of student """
        if type(attrs) == list and all(type(x) == str for x in attrs):
            # return
            return {item: self.__dict__.get(item) for item in attrs if item in self.__dict__}
        else:
            return self.__dict__
