#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle:
"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height
        The super call will use the logic of the __init__ of the
        Rectangle class.
        The width and height must be assigned to the value of size
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overriding to return [Square] + more information
        """
        cls = self.__class__.__name__
        size = self.height
        id = self.id
        x = self.x
        y = self.y
        return "[{}] ({}) {}/{} - {}".format(cls, id, x, y, size)

    @property
    def size(self):
        """property of size"""
        return self.width

    @size.setter
    def size(self, value):
        """
        The setter should assign (in this order) the width and the height
        with the same value.
        The setter should have the same value validation as the Rectangle
        for width and height
        No need to change the exception error message
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """refresh the values of square attributes"""
        args_list = ["id", "width", "x", "y"]
        if args and args[0] is not None:
            if len(args) > len(args_list):
                max_len = len(args_list)
            else:
                max_len = len(args)
            for i in range(max_len):
                setattr(self, args_list[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """creates a dictionary out of a given instance attributes"""
        sq_rect = dict()
        sq_rect["id"] = self.id
        sq_rect["x"] = self.x
        sq_rect["size"] = self.size
        sq_rect["y"] = self.y
        return sq_rect
