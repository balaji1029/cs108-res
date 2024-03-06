import numpy as np
import matplotlib.pyplot as plt
import time
"""
Import vectorized() and nonvectorized() from operation.py
Use the testcases given in the folder testcases to test your code here. You can print the result to check if it is correct.
"""
from operation import vectorized, nonvectorized
# read the testcases from the testcases/in folder
for i in range(2):

    matrix = np.genfromtxt(f'testcases/in/{i+1}.csv', delimiter=',', dtype=float)
    result = vectorized(matrix)
    print(result)



"""
Read the values from data/nonvectorized.txt and data/vectorized.txt into separate lists
Read values as float values.
"""
N_values = range(1, 101, 1)
with open('data/nonvectorized.txt', 'r') as f:
    nonvectorized_times = [float(line) for line in f]

with open('data/vectorized.txt', 'r') as f:
    vectorized_times = [float(line) for line in f]

plt.figure(figsize=(10,6)) # Don't change this line

"""
Draw a plot as specified in the problem statment using above values
"""
# Plot the execution times against N
plt.plot(N_values, nonvectorized_times, label='Non-vectorized')
plt.plot(N_values, vectorized_times, label='Vectorized')

t = 1e6
# Plot the reference lines
plt.plot(N_values, [N / t for N in N_values], label='N', linestyle='--')
plt.plot(N_values, [N**2 / t for N in N_values], label='N^2', linestyle='--')
plt.plot(N_values, [N**3 / t for N in N_values], label='N^3', linestyle='--')

# Add labels and legend
plt.xlabel('Input size N')
plt.ylabel('Execution time (s)')
plt.legend()

# save your plot in the end
plt.savefig('plot.png')
