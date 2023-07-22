#!/usr/bin/python3
"""
Class square.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class represents a square
    and inherits from the Rectangle class.

    Attributes (inherited from Rectangle):
        __width (int): The width of the square.
        __height (int): The height of the square (same as width).
        __x (int): The x-coordinate of the square's position.
        __y (int): The y-coordinate of the square's position.

    Methods:
        __init__(self, size, x=0, y=0, id=None):
            The constructor for the Square class.

            Args:
                size (int): The size of the square (width and height).
                x (int, optional): The x-coordinate
                of the square's position (default is 0).
                y (int, optional): The y-coordinate
                of the square's position (default is 0).
                id (int, optional): An optional
                parameter representing the ID of the square.

        update(self, *args, **kwargs):
            Assigns the provided key/value
            arguments to the corresponding attributes.

        __str__(self):
            Returns the string representation
            of the Square instance.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Args:
            size (int): The size of the square (width and height).
            x (int, optional): The x-coordinate
            of the square's position (default is 0).
            y (int, optional): The y-coordinate
            of the square's position (default is 0).
            id (int, optional): An optional
            parameter representing the ID of the square.

        Raises:
            ValueError: If size is less than or equal to 0.
            TypeError: If any of the arguments
            (size, x, y) is not an integer.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size attribute.
        """
        self.width = value
        self.height = value

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
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square instance.

        Returns:
            dict: A dictionary containing the attributes id, size, x, and y.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Returns the string representation
        of the Square instance.

        Returns:
            str: The formatted string
            representing the Square instance.
        """
        rect_x = self._Rectangle__x
        rect_y = self._Rectangle__y
        return f"[Square] ({self.id}) {rect_x}/{rect_y} - {self.width}"
