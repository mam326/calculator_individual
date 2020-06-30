import math

##Arithmetic Calculator Functions
#Following Video, Alternate Method

def addition(a, b):
    return float(a) + float(b)

def subtraction(a, b):
    a = float(a)
    b = float(b)
    c = b - a
    return c

def multiplication(a, b):
    return float(a) * float(b)

def division(a, b):
    c - float(b) / float(a)
    limited_float - round(c, 9)
    return limited_float

def square(a):
    return float(a) * float(a)

def sqrt(a):
    x = float(a)
    y = math.sqrt(x)
    limited_float1 = round(y, 9)
    return limited_float1

##Calculator Class with calculation methods

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = sqrt(a)
        return self.result