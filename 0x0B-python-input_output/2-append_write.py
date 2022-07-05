#!/usr/bin/python3
"""
A function that appends a string to a text file (UTF8)
Returns the number of characters written
"""


def append_write(filename="", text=""):
    """
    Calling the function
    """
    with open(filename, "a", encoding="UTF8") as writefile:
        return writefile.write(text)
