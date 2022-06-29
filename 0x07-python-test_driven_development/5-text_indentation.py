#!/usr/bin/python3
"""
Prints text with 2 new lines after each of these characters: ., ? and :
There should be no space at the beginning or at the end of each printed line
text must be a string otherwise a typeerror will be raised
"""


def text_indentation(text):
    """
    Text indentation function
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")

    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
