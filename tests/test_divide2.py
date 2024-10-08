# test_divide.py

from toto.divide2 import divide_without_raising
import math

def test_positive_division():
    assert divide_without_raising(10, 2) == 5
    assert divide_without_raising(1, 1) == 1

def test_negative_division():
    assert divide_without_raising(-10, 2) == -5
    assert divide_without_raising(10, -2) == -5

def test_zero_numerator():
    assert divide_without_raising(0, 2) == 0

def test_zero_denominator_positive():
    assert divide_without_raising(10, 0) == float('inf')

def test_zero_denominator_negative():
    assert divide_without_raising(-10, 0) == float('-inf')

def test_zero_zero_division():
    assert math.isnan(divide_without_raising(0, 0))

if __name__ == '__main__':
    test_positive_division()
    test_negative_division()
    test_zero_numerator()
    test_zero_denominator_positive()
    test_zero_denominator_negative()
    test_zero_zero_division()
    print("All tests passed!")
