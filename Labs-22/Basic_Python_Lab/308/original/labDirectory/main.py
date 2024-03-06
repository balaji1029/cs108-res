'''
    Geometry (Complex and Polar)
'''
import math

# import the classes


def modulus(c:Complex):
    '''return modulus of the complex number'''
    

def arg(c:Complex):
    '''return arg (angle) of the complex number'''
    

def abscissa(p:Polar):
    '''return abscissa of the polar point'''
    

def ordinate(p:Polar):
    '''return ordinate of the polar point'''
    

def distance(z1:Complex, z2:Complex):
    '''distance between points'''
    

if __name__ == '__main__':

    # you can use this area of code to check all the functions manually
    # one example of using the functions has been shown
    # run this using "python3 main.py"
    a = Complex(1,2)
    b = Complex(2,2)
    z = a + b # uses the overloaded add
    print(z)
    # print(modulus(z)) # you can call after you implement
    x = Polar(2,math.pi/3) # uses the overloaded power
    print(x ** 2)
