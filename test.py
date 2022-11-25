#!/usr/bin/python3
import unittest
from square import square
from cube import cube

class test(unittest.TestCase):

    def test_sq(self):
        n = 2
        result = square(n)
        self.assertEqual(result, 4)

    def test_cube(self):
        n = 2
        result = cube(n)
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
