#!/usr/bin/python3
"""
A function that returns an object (Python data structure)
represented by a JSON string:
"""


def from_json_string(my_str):
    """caling the function and importing json"""
    import json
    return json.loads(my_str)
