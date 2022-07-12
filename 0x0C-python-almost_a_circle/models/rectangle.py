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
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """position x getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """position y setter"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Update the class Rectangle by adding the public method def area(self):
        that returns the area value of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """Methode print instance"""
        ex, ye = self.x, self.y
        an, al = self.width, self.height
        print("\n" * ye + "\n".join(" " * ex + "#" * an for i in range(al)))

    def __str__(self):
        """
        Update the class Rectangle by overriding the __str__ method
        so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        first = f"({self.id}) {self.__x}/{self.__y}"
        second = f"{self.__width}/{self.__height}"
        return f"[Rectangle] {first} - {second}"

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by adding the public method
        def update(self, *args, **kwargs): that assigns a key/value argument
        to each attribute
        """
        count = 0
        if args is not None and len(args) != 0:
            for key in self.__dict__:
                if count >= len(args):
                    break
                else:
                    self.__dict__[key] = args[count]
                    count += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a
        """
        dic_rectangle = {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y,
                }
        return dic_rectangle
