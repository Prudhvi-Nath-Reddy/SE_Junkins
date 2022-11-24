#!/usr/bin/python3
import unittest
from square import square
from cube import cube

class test_code(unittest.TestCase):

    def sq_test(self):
        n = 2
        result = square(n)
        self.assertEqual(result, 5)

    def cube_test(self):
        n = 2
        result = cube(n)
        self.assertEqual(result, 900)


if __name__ == '__main__':
    unittest.main()
