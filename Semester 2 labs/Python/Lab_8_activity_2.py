'''
    Geometry (Complex and Polar)
    Author: Saksham Rathi
'''
import math

# import the classes
from complex import Complex
from polar import Polar

def modulus(c:Complex):
    return math.sqrt(c.x**2 + c.y**2)
    

def arg(c:Complex):
    return math.atan2(c.y,c.x)
    

def abscissa(p:Polar):
    return p.r * math.cos(p.t)
    

def ordinate(p:Polar):
    return p.r * math.sin(p.t)
    '''return ordinate of the polar point'''
    

def distance(z1:Complex, z2:Complex):
    '''distance between points'''
    return modulus(z1 - z2)
    

if __name__ == '__main__':

    # you can use this area of code to check all the functions manually
    # one example of using the functions has been shown
    # run this using "python3 main.py"
    a = Complex(1,2)
    b = Complex(2,2)
    z = a + b # uses the overloaded add
    print(z)
    print(modulus(z)) # you can call after you implement
    x = Polar(2,math.pi/3) # uses the overloaded power
    print(x ** 2)
