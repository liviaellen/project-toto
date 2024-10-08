import math
from toto.divide import divide_custom


def test_has_corect_arithmetic():
    assert divide_custom(2.0, 2.0) == 1.0, 'wrong basic arithmetics'

def test_handles_divide_by_zero_correctly():
    assert divide_custom(2., 0.) == float('inf')
    assert divide_custom(-2., 0.) == -1 * float('inf')
    assert math.isnan(divide_custom(0., 0.))
