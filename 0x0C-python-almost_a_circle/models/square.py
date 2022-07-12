#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle:
"""
from models.rectangle import Rectangle


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
        """overriding to return [Square] + more information"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

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
