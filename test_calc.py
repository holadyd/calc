import pytest
from calc import Calc


def test_calc():
    pass

def test_get_minus():
    calc = Calc()
    assert calc.get_minus(10,3) == 7
    assert calc.get_minus(6, 3) == 3

def test_get_sum():
    assert Calc().getSum(3,5) == 8

def test_gop():
    cal = Calc()
    assert cal.getGop(2,3) == 6
    assert cal.getGop(4,3) == 12

def test_calc_get_zegop():
    sut = Calc()
    ret = sut.getZegop(3)
    assert ret == 9
    
def test_getDivide():
    calc = Calc()
    ret = calc.getDivide(4, 2)
    assert ret == 2

def test_getDivide_by_zero():
    calc = Calc()
    with pytest.raises(ValueError):
        ret = calc.getDivide(4, 0)

