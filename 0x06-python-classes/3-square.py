#!/usr/bin/python3
"""defines a class square"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of the sides of a square
    """
    def __init__(self, size=0):
        """Initializes the Square
        Args:
            size (int): size of sides of square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """Calculates the square's area

        Returns:
            Area
        """
        return (self.__size) ** 2
