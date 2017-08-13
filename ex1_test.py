"""
Testing ex1
"""
from ex1 import *
import unittest

class ExTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_calc_plus(self):
        self.assertEqual(self.calc.calc_plus(2, 3), 5)

    def test_calc_minus(self):
        self.assertEqual(self.calc.calc_minus(12, 3), 9)
   
    def test_calc_multiply(self):
        self.assertEqual(self.calc.calc_multiply(2, 3), 6)

    def test_calc_divide(self):
        self.assertEqual(self.calc.calc_divide(15, 3), 5)

if __name__ == "__main__":
    unittest.main()
