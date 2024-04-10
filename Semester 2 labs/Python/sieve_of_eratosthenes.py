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

