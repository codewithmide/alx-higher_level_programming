#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """Returns a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        new_dict = {}

        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for i in json:
            self.__dict__.update({i: json[i]})
