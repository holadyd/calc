import pytest

from calc import Calc


def test_calc():
    pass

def test_getDivide():
    calc = Calc()
    ret = calc.getDivide(4, 2)
    assert ret == 2


def test_getDivide():
    calc = Calc()
    with pytest.raises(ValueError):
        ret = calc.getDivide(4, 0)

