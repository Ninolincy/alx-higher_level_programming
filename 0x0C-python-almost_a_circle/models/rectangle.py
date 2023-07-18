#!/usr/bin/python3
""" Module: Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of instance attributes"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            __width getter function
            Returns: width
        """
        return self.width

    @width.setter
    def width(self, value):
        """
            width setter function
            Args:
                value(int): value to be set
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            __height getter function
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter function
            Args:
                value(int): value to be set
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def y(self):
        """
            y getter function
            Return: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            y setter function
            Args:
                value(int): value to be set
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")

        self.__y = value

    @property
    def x(self):
        """
            x getter function
            Return: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            x setter function
            Return: x
        """
        return self.__x

    def x(self, value):
        """
            x setter function
            Args:
                value(int): value to be set
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")

        self.__x = value

    def area(self):
        """Computes area of a reactangle"""

        return self.__width * self.__height

    def display(self):
        """ Prints to stdout the Rectangle instance
        with the character #"""

        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string representation of a Rectangle instance."""

        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
