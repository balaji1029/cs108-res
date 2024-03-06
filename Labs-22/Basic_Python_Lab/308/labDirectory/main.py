import math
# import the classes
from complex import Complex
from polar import Polar
def modulus(c:Complex):
    '''return modulus of the complex number'''
    return round(math.sqrt((c.x)**2+(c.y)**2),2)
def arg(c:Complex):
    '''return arg (angle) of the complex number'''
    if c.x==0 and c.y>0:
      return 1.57
    if c.x==0 and c.y<0:
      return -1.57
    arg1=math.atan((c.y)/(c.x))
    if c.x>0:
      return round(arg1,2)
    if c.y>0 and c.x<0:
      return round(math.pi + arg1,2)
    if c.y<0 and c.x<0:
      return round(arg1 - math.pi,2)
def abscissa(p:Polar):
    '''return abscissa of the polar point'''
    return round((p.r)*math.cos(p.t),2)
def ordinate(p:Polar):
    '''return ordinate of the polar point'''
    return round((p.r)*math.sin(p.t),2)
def distance(z1:Complex, z2:Complex):
    '''distance between points'''
    return round(math.sqrt((z1.x-z2.x)**2+(z1.y-z2.y)**2),2)
if __name__ == '__main__':
    # you can use this area of code to check all the functions manually
    # one example of using the functions has been shown
    # run this using "python3 main.py"
    a = Complex(1,2)
    b = Complex(2,2)
    z = a + b # uses the overloaded add
    print(arg(z))
    # print(modulus(z)) # you can call after you implement
    x = Polar(2,math.pi/3) # uses the overloaded power
    print(abscissa(x))
