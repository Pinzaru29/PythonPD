# test_functions.py
import unittest
from functions import *

class TestIntOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(subtract(5, 5), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)
        self.assertEqual(multiply(-3, 2), -6)

    def test_divide(self):
        self.assertEqual(divide(8, 4), 2)
        self.assertEqual(divide(10, 3), 3.3333333333333335)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

if __name__ == '__main__':
    unittest.main(exit=True)
