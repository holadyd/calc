class Calc:

    def getDivide(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Can't divide by zero")
        return numerator/denominator