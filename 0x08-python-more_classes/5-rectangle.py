#!/usr/bin/python3
"""
Create a rectangle class
"""


class Rectangle:
    """
    The class rectangle
    """

    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        The width getter
        Returns the self width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        defining the width setter
        Raise a TypeError and ValueError if some conditions are not met
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        The height getter
        Returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The height setter
        Raise a TypeError and ValueError if soe conditions are not met
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Public instance method: def area(self): that returns the rectangle area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Public instance method that returns the rectangle perimeter
        if width or height is equal to 0, perimeter is equal to 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        print() and str() should print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        st = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return st

    def __repr__(self):
        """
        return a string representation of the rectangle
        to recreate a new instance
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
        deletes an instance
        """
        print("Bye rectangle...")
