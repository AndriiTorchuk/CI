"""
Exercise 7: Test
"""

from ex7 import sortfunc
import unittest

class test_sortfunc(unittest.TestCase):
    def test_normal(self):
        res = sortfunc([3, 7, 2, 4, 5, 8, 6, 1])
        self.assertEqual(res, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_abc(self):
        res = sortfunc(['a', 'c', 'd', 'b', 'f'])
        self.assertEqual(res, ['a', 'b', 'c', 'd', 'f'])

unittest.main()


