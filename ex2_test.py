"""
Exercise 1: Test
"""
from ex2 import *
import unittest

class Test_calcu(unittest.TestCase):
    def setUp(self):
        self.calc = calculate()
    def test_adding_res(self):
        self.assertEqual(6, self.calc.add(2, 4))


if __name__ == "__main__":
    unittest.main()

