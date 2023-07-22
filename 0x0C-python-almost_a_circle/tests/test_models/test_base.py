#!/usr/bin/python3
"""
Test TestBaseClass class.
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_new_instance_with_id(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.id, 1)

        r2 = Rectangle(2, 4)
        self.assertEqual(r2.id, 2)

    def test_create_new_instance_with_custom_id(self):
        s = Square(5, id=10)
        self.assertEqual(s.id, 10)

    def test_create_new_instance_with_default_id(self):
        s = Square(3)
        self.assertEqual(s.id, 1)

    def test_to_json_string_with_empty_list(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_with_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_from_json_string_with_valid_data(self):
        json_str = '[{"id": 1, "width": 5, "height": 10, "x": 0, "y": 0}, '
        '{"id": 2, "size": 3, "x": 0, "y": 0}]'
        lst = Base.from_json_string(json_str)
        self.assertEqual(type(lst), list)
        self.assertEqual(len(lst), 2)

    def test_from_json_string_with_empty_list(self):
        self.assertEqual(Base.from_json_string('[]'), [])

    def test_from_json_string_with_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_load_from_file_with_valid_data(self):
        r = Rectangle(5, 10)
        s = Square(3)
        Rectangle.save_to_file([r, s])
        lst = Rectangle.load_from_file()
        self.assertEqual(type(lst), list)
        self.assertEqual(len(lst), 2)

    def test_load_from_file_with_nonexistent_file(self):
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])

    def test_load_from_file_csv_with_valid_data(self):
        r = Rectangle(5, 10)
        s = Square(3)
        Rectangle.save_to_file_csv([r, s])
        lst = Rectangle.load_from_file_csv()
        self.assertEqual(type(lst), list)
        self.assertEqual(len(lst), 2)
        self.assertEqual(type(lst[0]), Rectangle)
        self.assertEqual(type(lst[1]), Square)

    def test_load_from_file_csv_with_nonexistent_file(self):
        lst = Rectangle.load_from_file_csv()
        self.assertEqual(lst, [])

    def test_save_to_file_csv_with_valid_data(self):
        r = Rectangle(5, 10)
        s = Square(3)
        Rectangle.save_to_file_csv([r, s])
        with open("Rectangle.csv", 'r') as file:
            content = file.read()
            self.assertEqual(content, '1,5,10,0,0\n2,3,0,0')

    def test_save_to_file_csv_with_invalid_data(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv("Not a list")

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
