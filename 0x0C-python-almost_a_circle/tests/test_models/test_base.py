#!/usr/bin/python3
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """ Unit tests for testing instantiation of the Base class """

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_id_automatically(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertTrue(b1, self.id == 1)
        self.assertTrue(b2, self.id == 2)
        self.assertTrue(b3, self.id == 3)
        self.assertTrue(b4, self.id == 12)
        self.assertTrue(b5, self.id == 4)

    def test_1_id(self):
        Base._Base__nb_objects = 0
        bas = Base()
        self.assertEqual(bas.id, 1)
        t1 = Base(22)
        self.assertEqual(t1.id, 22)
        t2 = Base(-33)
        self.assertEqual(t2.id, -33)
        t3 = Base()
        self.assertEqual(t3.id, 2)

    def test_to_json_string(self):
        dic1 = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        dic2 = {'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10}
        string = Base.to_json_string([dic1, dic2])
        self.assertTrue(type(dic1) == dict)
        self.assertTrue(type(dic2) == dict)
        self.assertTrue(type(string) == str)
        self.assertTrue(string,
                        [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8},
                         {'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10}])

    def test_empty_to_json_string(self):
        dic3 = {}
        stri = Base.to_json_string([dic3])
        self.assertTrue(type(stri) == str)
        self.assertTrue(len(dic3) == 0)
        self.assertTrue(stri, [])

    def test_none_to_json_string(self):
        dic4 = None
        stri = Base.to_json_string([dic4])
        self.assertTrue(type(stri) == str)
        self.assertTrue(stri, [])

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 9)
        r2 = Rectangle(2, 4, 6, 8, 10)
        sq1 = Square(2, 3, 4, 5)
        sq2 = Square(6, 7, 8, 9)
        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([sq1, sq2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([r1.to_dictionary(), r2.to_dictionary()]),
                file.read())
        with open("Square.json", "r") as f:
            self.assertEqual(
                json.dumps([sq1.to_dictionary(), sq2.to_dictionary()]),
                f.read())

    def test_empty_save_to_file(self):
        Rectangle.save_to_file([])
        Square.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())
        with open("Square.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_none_save_to_file(self):
        Rectangle.save_to_file(None)
        Square.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())
        with open("Square.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_one_save_to_file(self):
        sq1 = Square(1)
        sq2 = Square(1, 1)
        Square.save_to_file([sq1, sq2])
        with open("Square.json", "r") as file:
            self.assertEqual(
                json.dumps([sq1.to_dictionary(), sq2.to_dictionary()]),
                file.read())

    def test_from_json_string(self):
        list1 = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        jsonlist1 = Base.from_json_string(list1)
        self.assertTrue(type(list1) == str)
        self.assertTrue(type(jsonlist1) == list)
        self.assertTrue(type(jsonlist1[0]) == dict)
        self.assertTrue(jsonlist1,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])
        self.assertTrue(jsonlist1[0],
                        {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_empty_from_json_string(self):
        list2 = ""
        jsonlist2 = Base.from_json_string(list2)
        self.assertTrue(type(jsonlist2) == list)
        self.assertTrue(jsonlist2 == [])

    def test_none_from_json_string(self):
        list3 = None
        jsonlist3 = Base.from_json_string(list3)
        self.assertTrue(type(jsonlist3) == list)
        self.assertTrue(jsonlist3 == [])

    def test_create(self):
        rec1 = Rectangle(2, 3, 4, 5, 9)
        dic = rec1.to_dictionary()
        rec2 = Rectangle.create(**dic)
        self.assertEqual(str(rec1), '[Rectangle] (9) 4/5 - 2/3')
        self.assertEqual(str(rec2), '[Rectangle] (9) 4/5 - 2/3')
        self.assertIsNot(rec1, rec2)

    def test_load_from_file(self):
        rec1 = Rectangle(5, 7, 2, 4, 9)
        rec2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([rec1, rec2])
        recs = Rectangle.load_from_file()
        self.assertEqual(len(recs), 2)
        for k, v in enumerate(recs):
            if k == 0:
                self.assertEqual(str(v), '[Rectangle] (9) 2/4 - 5/7')
            if k == 1:
                self.assertEqual(str(v), '[Rectangle] (98) 2/2 - 2/4')

    def test_square_save_to_file(self):
        sq1 = Square(2, 3, 4, 5)
        sq2 = Square(6, 7, 8, 9)
        Square.save_to_file([sq1, sq2])
        sqs = Square.load_from_file()
        self.assertEqual(len(sqs), 2)
        for i, j in enumerate(sqs):
            if i == 0:
                self.assertEqual(str(j), '[Square] (5) 3/4 - 2')
            if i == 1:
                self.assertEqual(str(j), '[Square] (9) 7/8 - 6')

    def test_none_load_from_file(self):
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

    def test_square_load_from_file(self):
        Square.save_to_file(None)
        sqs = Square.load_from_file()
        self.assertEqual(type(sqs), list)
        self.assertEqual(len(sqs), 0)

    def test_empty_load_from_file(self):
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)


if __name__ == "__main__":
    unittest.main()
