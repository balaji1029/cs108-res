'''
You have been given class-based implementations of Complex and Polar forms of numbers.

Go through these classes. The functions that have been implemented are all overloaded

functions (essentially, this means we extend the definition of some operator, for example

addition in order to directly add objects of this class).



The "__init__" function is just a constructor for the Complex class. The "__str__" function

tells Python that when it wants to convert an instance of Complex class to a string (when you

try to print a complex number "z" using print(z)) it should use this function.



The others are for arithmetic operations, as explained below. Few example calls have been added

to the main function within main.py as well for you to see. You can experiment as much as you

like in the main function area within main.py.



For example, look at the "__add__" function in the Complex class. This function takes two

arguments, one being a reference to itself (self) and the other being "a" (a Complex number

for our case). So this function is telling Python that when it encounters an expression of

the form "c + z", where both "c" and "z" are instances of Complex class, then it has to use

this function (with arguments being passed as self = c and a = z) and then return the result

as dictated by the function. In this case, the result is an addition of each component of the

complex numbers, and we get another complex number which is the sum of c and z. Similarly, the

"__sub__" function has been defined for subtraction.



Moving on to the Polar class, the function "__mul__" enables taking product of two instances of

the Polar class. As an example, consider two instances of Polar class a(2,1) and b(3,2). Note

that in Polar representation, we have considered the angle "theta" to be in radians. So now if

we try to calculate "a * b", Python will use the overloaded multiplication operation and result

in a new Polar class instance as return value with r = 2 * 3 = 6 and t = 1 + 2 = 3.

Similarly, the "__pow__" function has been defined for exponentiation of a polar number.



What you need to do:



ONLY EDIT THE FILE "main.py".



First import the Complex and Polar classes into main.py.



Within main.py, there are several functions which are often used when working with Complex and

Polar numbers. You need to complete the implementations as indicated below. Refer to the links

if you are confused about the definition of any function.



(1) modulus: modulus of the given complex number. Return type: float. Range: [0, infty).



(2) arg: argument (in radians) of the given complex number. Return type: float.

Range: (-pi, pi].



(3) abscissa: x-coordinate of the polar number. Return type: float. Range: (-infty,infty).



(4) ordinate: y-coordinate of the polar number. Return type: float. Range: (-infty, infty).



(5) distance: distance between two complex numbers. Return type: float. Range: [0, infty).



If you want to run any of the testcases locally, note the following:

1. You can call the appropriate function (with appropriate arguments) in the main program

section of main.py

2. The first line of each of the testcase file is the number of testcases included within it

so it is not relevant to the program, it is only for the autograder

3. The arguments in each following line are the "a" and "b" arguments if the input to the tested

function is a complex number, and the "r" and "t" arguments if the input is a polar 

3. As an example, suppose you want to check abscissa function



--------------------------------------------------------------------------

                References/Links



1. operator overloading

https://www.programiz.com/python-programming/operator-overloading

2. forms of complex numbers

https://www.geeksforgeeks.org/polar-and-exponential-forms-of-complex-numbers/

https://www.cuemath.com/numbers/polar-form-of-complex-numbers/

3. python math module

https://docs.python.org/3/library/math.html

4. complex numbers functions

modulus: https://www.cuemath.com/algebra/modulus-of-complex-number/

arg: https://www.cuemath.com/numbers/argument-of-complex-number/

abscissa: https://www.mathsisfun.com/definitions/abscissa.html

ordinate: https://www.mathsisfun.com/definitions/ordinate.html
'''

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
