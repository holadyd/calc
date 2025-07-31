from calc import Calc


def test_calc():
    pass

def test_getDevide():
    calc = Calc()
    ret = calc.getDevide(4, 2)
    assert ret == 2

