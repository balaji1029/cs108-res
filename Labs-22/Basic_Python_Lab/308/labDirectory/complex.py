'''
    Complex Numbers
'''

class Complex:

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __str__(self):
        return f"{self.x} + i{self.y}"

    def __add__(self, a):
        return Complex(self.x + a.x, self.y + a.y)

    def __sub__(self, a):
        return Complex(self.x - a.x, self.y - a.y)
