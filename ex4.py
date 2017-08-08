"""
Exercise 4
"""

from ex2 import *
import unittest

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = calculate()
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2,2))

unittest.main()
