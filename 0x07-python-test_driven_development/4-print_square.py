#!/usr/bin/python3
"""
a function that prints a square with the character #
size is the size length of the square
size must be an integer
"""


def print_square(size):
    """
    prints a square shaped character with #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#" * size for rows in range(size)]))
