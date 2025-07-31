from calc import Calc


def test_calc():
    pass


def test_calc_get_zegop():
    sut = Calc()
    ret = sut.getZegop(3, 3)
    assert ret == 9
