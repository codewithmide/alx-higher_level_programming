#!/usr/bin/python3
"""
A function that returns an object (Python data structure)
represented by a JSON string:
"""


def save_to_json_file(my_obj, filename):
    """caling the function and importing json"""
    import json
    with open(filename, 'w', encoding="UTF8") as jsonsave:
        jsonsave.write(json.dumps(my_obj))
