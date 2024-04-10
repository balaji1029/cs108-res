'''
In this problem, we will implement the Sieve of Eratosthenes method for computing primes up to

a specified number (les than or equal to a given number).



You need to collect all the prime numbers in a list and print this list (sorted order). The

evaluation will check your output list, though the implementation efficiency is also important.



For an example, the python script will be run using the following command:

python3 main.py 10



Here the input (10) is the number given, so the output should be a list of all prime numbers

that are less than or equal to 10:

[2, 3, 5, 7]



You will need to use a function from the sys library to implement the command line parameter.



This problem seems quite complicated, so let's break it down into steps:



Step 1:

First we will need a list of numbers from 2 to the given number, so that we can select the

primes out from this based on the method.



Step 2:

We need to keep iterating over this list till we have no more numbers to check. We also need

a list to store the output.



Step 3:

In the Sieve of Eratosthenes method, the next uncrossed/valid number is prime and is

recorded, and then from among the remaining numbers (yet to check), all the multiples

of this recorded number are removed. In this step, try using list comprehension (check

reference 2).



--------------------------------------------------------------------------

                Additional



This section is related to an alternate approach to this problem which uses some extra functions

that python provides for commonly used functionality related to lists and collections. This is

PURELY for extra practice and additional knowledge, and will NOT be tested in exams. So you can

consider this as only for reference purposes.



Though it is possible to achieve this by using one loop itself along with list comprehension,

try to come up with an answer that uses as less loops as possible. This will be checked based

on the amount of time your program takes to find the list. A few testcases might fail if a lot

of loops are used. Try to look for a solution that uses lambda functions, map, reduce and

filter.



If you want to use reduce, you can add this line below the "import sys" line:

from functools import reduce



--------------------------------------------------------------------------

                References/Links



1. Sieve of Eratosthenes

https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

2. list comprehension

https://www.w3schools.com/python/python_lists_comprehension.asp

3. map, filter and reduce

https://towardsdatascience.com/pythons-map-filter-and-reduce-functions-explained-2b3817a94639

https://www.analyticsvidhya.com/blog/2021/07/python-most-powerful-functions-map-filter-and-reduce-in-5-minutes/

https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce
'''
'''
    Sieve of Eratosthenes
    Author: Saksham Rathi
'''

import sys
from time import process_time_ns

# read the parameter from command line using sys
if len(sys.argv) != 2:
    print("Usage: python main.py n")
    sys.exit()

n = int(sys.argv[1])
if n == 1:
    print([])
    sys.exit()
if n < 3:
    print([2])
    sys.exit()
potential_candidates = list(range(3, n+1, 2))
potential_candidates.pop(0)
primes = [2, 3]
current_index = 1

time_start = process_time_ns()
while True:
    curr_number = primes[current_index]
    if curr_number*curr_number > n:
        primes += potential_candidates
        break
    # potential_candidates = list(filter(lambda x: x%curr_number != 0, potential_candidates))
    potential_candidates = [num for num in potential_candidates if num%curr_number != 0]
    if potential_candidates:
        primes.append(potential_candidates[0])
        potential_candidates.pop(0)
        current_index += 1
    else:
        break
print(primes)
time_stop = process_time_ns()
# print("Elapsed time during the whole program in seconds:", time_stop-time_start)  

# your implementation for printing the list of prime numbers

