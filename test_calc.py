from calc import Calc


def test_calc():
    calc = Calc()
    a=1
    b=2
    c=3
    assert a+b+c == calc.getSumSum(a,b,c)

