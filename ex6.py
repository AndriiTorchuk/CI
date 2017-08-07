"""
Exercise 6: Methods
"""

import unittest
# assertAlmostEqual Method
class testt(unittest.TestCase):
    def test_almost_equal(self):
        self.assertAlmostEqual(1, 1.2, delta=0.5)
# assertRaises Method
class testt2(unittest.TestCase):
    def test_assertraises(self):
        self.assertRaises(ValueError, int, "a")
# assertDictContainsSubset Method
class testt3(unittest.TestCase):
    def test_assertDict(self):
        expected = {'a': 'b'}
        actual  = {'a': 'b', 'c':'d'}
        self.assertDictContainsSubset(expected, actual)
# assertGreate Method
class testt4(unittest.TestCase):
    def test_greater(self):
        self.assertGreater(3, 2)

unittest.main()
