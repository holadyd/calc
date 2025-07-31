from calc import Calc


def test_calc():
    pass

def test_gop():
    cal = Calc()
    assert cal.getGop(2,3) == 6
    assert cal.getGop(4,3) == 12