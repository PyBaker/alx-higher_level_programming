#!/usr/bin/python3
""" Module ./9-student.py
    Defines a Student class with fields and methods

    Attributes:
        first_name
        second_name
        age

    Methods:
        to_json(self) --> retrieves a dictionary representation of Student

"""


class Student:
    """ Defines a student class """

    def __init__(self, first_name, second_name, age):
        """ initiallises student attributes

            Args:
                first_name (str): The first name of the student.
                last_name (str): The last name of the student.
                age (int): The age of the student.
        """

        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def to_json(self):
        """ returns dictionary representation of student """
        return self.__dict__
