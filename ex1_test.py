"""
Testing ex1
"""

import ex1

def test_calc_plus():
    res1 = ex1.calc_plus(2, 2)
    assert res1 == 4

def test_calc_minus():
    res2 = ex1.calc_minus(10, 5)
    assert res2 == 5

def test_calc_multiply():
    res3 = ex1.calc_multiply(3, 5)
    assert res3 == 15

def test_calc_divide():
    res4 = ex1.calc_divide(8, 4)
    assert res4 == 2
