"""
Testing ex1
"""
from ex1 import *
import unittest

class mytest(unittest.TestCase):
    def test_calc_plus(self):
        self.assertEqual(calc_plus(2, 3), 5)

    def test_calc_minus(self):
        self.assertEqual(calc_minus(12, 3), 9)
   
    def test_calc_multiply(self):
        self.assertEqual(calc_multiply(2, 3), 6)

    def test_calc_divide(self):
        self.assertEqual(calc_divide(15, 3), 5)

unittest.main()
