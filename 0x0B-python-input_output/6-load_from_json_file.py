#!/usr/bin/python3
"""
A function that creates an Object from a “JSON file”:
"""


def load_from_json_file(filename):
    """Methode load fron json file"""
    import json
    with open(filename, "r", encoding="UTF8") as loadjson:
        return json.load(loadjson)
