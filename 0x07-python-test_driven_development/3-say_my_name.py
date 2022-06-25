#!/usr/bin/python3
"""
a function that prints My name is <first name> <last name>
The first name must be a string
The last name must be a string
"""


def say_my_name(first_name, last_name=""):
    """
    Defining the function name and arguments to be taken
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("first_name must be a string")

    print(f"My name is {first_name} {last_name}")
