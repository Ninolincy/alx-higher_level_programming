#!/usr/bin/python3
"""
Test square class.
"""


import unittest
from models.square import Square
from models.base import Base


class TestSquareClass(unittest.TestCase):
    def test_create_new_square(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_create_new_square_with_custom_id(self):
        s = Square(5, 0, 0, 100)
        self.assertEqual(s.id, 100)

    def test_create_new_square_with_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-5)

    def test_create_new_square_with_negative_x(self):
        with self.assertRaises(ValueError):
            Square(5, -2)

    def test_create_new_square_with_negative_y(self):
        with self.assertRaises(ValueError):
            Square(5, 0, -3)

    def test_area_method(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str_method(self):
        s = Square(5, 2, 3, 100)
        self.assertEqual(str(s), "[Square] (100) 2/3 - 5")

    def test_update_with_args(self):
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_with_kwargs(self):
        s = Square(5)
        s.update(size=10, x=2, y=3)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_to_dictionary_method(self):
        s = Square(5, 2, 3, 100)
        expected_dict = {'id': 100, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
