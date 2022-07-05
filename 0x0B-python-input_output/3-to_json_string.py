#!/usr/bin/python3
"""
A function that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """caling the function and importing json"""
    import json
    return json.dumps(my_obj)
