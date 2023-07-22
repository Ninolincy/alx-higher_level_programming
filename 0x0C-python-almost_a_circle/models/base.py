#!/usr/bin/python3

"""
The Base class.
"""


import json
import csv


class Base:
    """
     is the foundation for all other
    classes in the project and provides a mechanism for managing the 'id'
    attribute of instances.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int, optional): An optional parameter
            representing the ID of the instance. If provided, the 'id'
            attribute of the instance will be set to this value.
            If not provided, a new ID will be generated and
            assigned to the instance by incrementing the
            '__nb_objects' class attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.

        Raises:
            TypeError: If list_objs is not a list of Base instances.
        """
        if list_objs is None:
            list_objs = []

        if not isinstance(list_objs, list):
            t_error = "list_objs must be a list "
            t_error2 = "of instances that inherit from Base"
            raise TypeError(t_error + t_error2)

        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of instances represented by the JSON string.

        Args:
            json_string (str): The JSON string representing
            a list of dictionaries.

        Returns:
            list: The list of instances represented by json_string.

        Raises:
            ValueError: If json_string is not a valid JSON string.
        """
        if json_string is None or json_string == "":
            return []

        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON string: " + str(e))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already
        set based on the provided dictionary.

        Args:
            **dictionary: Keyworded argument list
            representing attribute key/value pairs.

        Returns:
            Base: An instance of the class with
            attributes set according to the provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unknown class type")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a JSON file.

        Returns:
            list: A list of instances based on the JSON data.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                list_dicts = cls.from_json_string(json_data)
                return [cls.create(**dict_obj) for dict_obj in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes and saves a list of instances to a CSV file.

        Args:
            list_objs (list): A list of instances.

        Raises:
            TypeError: If list_objs is not a list of instances.
        """
        if not isinstance(list_objs, list):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row_data = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row_data = [obj.id, obj.size, obj.x, obj.y]
                else:
                    raise ValueError("Unknown class type")

                writer.writerow(row_data)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes and loads instances from a CSV file.

        Returns:
            list: A list of instances based on the data in the CSV file.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                instance_list = []

                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]),
                                       int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]), int(row[2]),
                                       int(row[3]), int(row[0]))
                    else:
                        raise ValueError("Unknown class type")

                    instance_list.append(instance)

                return instance_list
        except FileNotFoundError:
            return []
