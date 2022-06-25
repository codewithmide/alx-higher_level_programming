#!/usr/bin/python3
"""
Module 0-add_integer
Contains one method that returns an int sum
Accepts two values, whether int or float, and casts them to int before adding
"""


def add_integer(a, b=98):
    """ Adds 2 integers
    Args: a, b
    Return a + b"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
