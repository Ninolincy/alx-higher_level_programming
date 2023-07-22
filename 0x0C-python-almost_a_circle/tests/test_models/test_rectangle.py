#!/usr/bin/python3
"""
Test TestRectangleClass class.
"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    def test_create_new_rectangle(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_create_new_rectangle_with_custom_id(self):
        r = Rectangle(5, 10, 0, 0, 100)
        self.assertEqual(r.id, 100)

    def test_create_new_rectangle_with_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

    def test_create_new_rectangle_with_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -10)

    def test_create_new_rectangle_with_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2)

    def test_create_new_rectangle_with_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 0, -3)

    def test_area_method(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_str_method(self):
        r = Rectangle(5, 10, 2, 3, 100)
        self.assertEqual(str(r), "[Rectangle] (100) 2/3 - 5/10")

    def test_update_with_args(self):
        r = Rectangle(5, 10)
        r.update(10)
        self.assertEqual(r.id, 10)

    def test_update_with_kwargs(self):
        r = Rectangle(5, 10)
        r.update(width=20, height=30, x=2, y=3)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_to_dictionary_method(self):
        r = Rectangle(5, 10, 2, 3, 100)
        expected_dict = {'id': 100, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertDictEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
