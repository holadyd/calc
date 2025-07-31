class Calc:

    def getSumSum(self, a, b, c):
        return a+b+c
 
    def getDivide(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Can't divide by zero")
        return numerator/denominator
      
    def get_minus(self, a, b):
        return a - b

    def getSum(self,a,b):
        return a + b

    def getGop(self, a, b):
        return a*b

    def getZegop(self, num):
        return num * num

