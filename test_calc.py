from calc import Calc

def test_calc():
    pass

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

