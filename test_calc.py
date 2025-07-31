from calc import Calc


def test_calc():
    pass

def test_get_minus():
    calc = Calc()
    ret = calc.get_minus(10,3)
    assert ret == 7
