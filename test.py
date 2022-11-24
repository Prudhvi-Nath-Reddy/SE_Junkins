#!/usr/bin/python3
import unittest
from square import square
from cube import cube

class test_code(unittest.TestCase):

    def test_sq_test(self):
        n = 2
        result = square(n)
        self.assertEqual(result, 4)

    def test_cube_test(self):
        n = 2
        result = cube(n)
        self.assertEqual(result, 90)


if __name__ == '__main__':
    unittest.main()
