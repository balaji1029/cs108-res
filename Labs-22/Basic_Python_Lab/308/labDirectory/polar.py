'''
    Polar Coordinates
'''

class Polar:

    def __init__(self, a, b):
        self.r = a
        self.t = b

    def __str__(self):
        return f"({self.r},{self.t})"

    def __mul__(self, a):
        return Polar(round(self.r * a.r,2), round(self.t + a.t,2))

    def __pow__(self, a):
        return Polar(round(self.r ** a,2), round(self.t * a,2))
