#!/usr/bin/python3
"""
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Call the super class with id
        The super call with use the logic of the __init__ of the Base class
        Assign each argument width, height, x and y to the right attribute
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        width property getter
        """
        return self.__width

    @property
    def height(self):
        """
        height property getter
        """
        return self.__height

    @property
    def x(self):
        """
        x property getter
        """
        return self.__x

    @property
    def y(self):
        """
        y property getter
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not (isinstance(value, int)):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if not (isinstance(value, int)):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """
        x setter
        """
        if not (isinstance(value, int)):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        if not (isinstance(value, int)):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        Update the class Rectangle by adding the public method def area(self):
        that returns the area value of the Rectangle instance.
        """
        return self.__width * self.__height
