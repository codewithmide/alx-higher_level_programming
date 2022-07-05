#!/usr/bin/python3
"""
A function that writes a string to a text file (UTF8)
Returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Calling the function
    """
    with open(filename, mode="w", encoding="UTF8") as writefile:
        return writefile.write(text)
