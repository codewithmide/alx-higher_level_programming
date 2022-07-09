#!/usr/bin/python3
"""
Class Base:
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None):
"""
import json


class Base:
    """created the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Update the class Base by adding the static method
        def to_json_string(list_dictionaries):
        that returns the JSON string representation of list_dictionaries:
        """
        if list_dictionaries is None:
            return "[]"
        else:
            string = json.dumps(list_dictionaries)
            return string
