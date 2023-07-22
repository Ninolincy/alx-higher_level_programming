#!/usr/bin/python3
"""
Class Rectangle.
"""


from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class represents a rectangle
    and inherits from the Base class.

    Attributes:
        __width (int): The private width of the rectangle.
        __height (int): The private height of the rectangle.
        __x (int): The private x-coordinate of
        the rectangle's position.
        __y (int): The private y-coordinate of
        the rectangle's position.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            The constructor for the Rectangle class.

            Args:
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.
                x (int, optional): The x-coordinate of
                the rectangle's position (default is 0).
                y (int, optional): The y-coordinate of
                the rectangle's position (default is 0).
                id (int, optional): An optional
                parameter representing the ID of the rectangle.
        """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of
            the rectangle's position (default is 0).
            y (int, optional): The y-coordinate of
            the rectangle's position (default is 0).
            id (int, optional): An optional
            parameter representing the ID of the rectangle.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer.")
        if width <= 0:
            raise ValueError("width must be > 0.")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer.")
        if height <= 0:
            raise ValueError("height must be > 0.")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer.")
        if x < 0:
            raise ValueError("x must be >= 0.")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer.")
        if y < 0:
            raise ValueError("y must be >= 0.")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """
        Get width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer.")
        if value <= 0:
            raise ValueError("width must be > 0.")
        self.__width = value

    @property
    def height(self):
        """
        Get height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer.")
        if value <= 0:
            raise ValueError("height must be > 0.")
        self.__height = value

    @property
    def x(self):
        """
        Get x-coordinate
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        Set x-coordinate
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer.")
        if value < 0:
            raise ValueError("x must be >= 0.")
        self.__x = value

    @property
    def y(self):
        """
        Get y-coordinate
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Set y-coordinate
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be >= 0.")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area
        value of the Rectangle instance.

        Returns:
            int: The area value of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the Rectangle instance using the character '#'.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Assigns the provided key/value arguments
        to the corresponding attributes.

        Args:
            *args: Variable-length argument list.
            (Unused in this version of the method)
            **kwargs: Keyworded argument list
            representing attribute key/value pairs.
        """
        if args:
            return

        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'width' in kwargs:
            self.__width = kwargs['width']
        if 'height' in kwargs:
            self.__height = kwargs['height']
        if 'x' in kwargs:
            self.__x = kwargs['x']
        if 'y' in kwargs:
            self.__y = kwargs['y']

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle instance.

        Returns:
            dict: A dictionary containing the attributes
            id, width, height, x, and y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Returns the string representation
        of the Rectangle instance.

        Returns:
            str: The formatted string
            representing the Rectangle instance.
        """

        st_width = self.__width
        st_height = self.__height
        st_id = self.id
        st_x = self.__x
        st_y = self.__y
        return f"[Rectangle] ({st_id}) {st_x}/{st_y} - {st_width}/{st_height}"
