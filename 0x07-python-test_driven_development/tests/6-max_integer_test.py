#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_regular(self):
        l = [1, 2, 4, 5, 8]
        result = max_integer(l)
        self.assertEqual(result, 8)

    def test_not_int(self):
        l = ["i", "j", 4]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty(self):
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_negative(self):
        l = [-5, -3, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_float(self):
        l = [1, 5.5, 3]
        result = max_integer(l)
        self.assertEqual(result, 5.5)

    def test_not_list(self):
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        l = [30]
        result = max_integer(l)
        self.assertEqual(result, 30)

    def test_identical(self):
        l = [2, 2, 2, 2, 2]
        result = max_integer(l)
        self.assertEqual(result, 2)

    def test_strings(self):
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

    def test_none(self):
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
