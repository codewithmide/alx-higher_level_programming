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
        self.size = size

    def area(self):
        """Calculates the square's area

        Returns:
            Area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of size
        Returns:
           The size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size
        Args:
            value (int): The size of the sides of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """Prints the square

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__size):
                print("".join(["#" for j in range(self.__size)]))
