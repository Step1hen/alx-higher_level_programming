#!/usr/bin/python3
"""
This module consist of the "Square" class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a sq."""

    def __init__(self, size, x=0, y=0, id=None):
        """Init a new Sq.
        Args:
            size (int): The size of the new Sq.
            x (int): The x coordinate of the new Sq.
            y (int): The y coordinate of the new Sq.
            id (int): The identity of the new Sq.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Sq."""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Sq.
        Args:
            *args (ints): New attr values.
                - 1st arg reps id attr
                - 2nd arg reps size attr
                - 3rd arg reps x attr
                - 4th arg reps y attr
            **kwargs (dict): New key/value pairs of attrs.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dict rep of the Sq."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def display(self):
        """Print the square with '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the print() and str() rep of a Sq."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
