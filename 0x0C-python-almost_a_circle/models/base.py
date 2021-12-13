#!/usr/bin/python3
""" Module ./base.py
    Initialises a Base Class
"""
import json


class Base:
    """ Defines a Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialises Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON representation of list """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes json string to list_objs file """
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w", encoding="UTF-8") as file:
            if list_objs is None:
                json.dump([], file)
            else:
                json.dump(list_objs, file)

    @classmethod
    def create(cls, **dictionary):
        super().__init__(34, 23, 10, 3)
        return cls.update(dictionary)
