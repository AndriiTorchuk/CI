"""
Exercise 3
"""
from ex2 import *
import unittest



def add(self, x, y):
    if type(x) == int and type(y) == int:
        return x + y
    else:
        raise TypeError("invalid type: {} and {}".format(type(x), type(y)))

class Test_calcu(unittest.TestCase):
    def setUp(self):
        self.calc = calculate()
    def test_adding_res(self):
        self.assertEqual("hello", self.calc.add("he", "llo"))


unittest.main()


