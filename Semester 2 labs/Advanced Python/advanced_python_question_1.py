'''
The Matrix
--------------------------------------------------------------------------

Some helpful References:

1. statistics

https://numpy.org/doc/stable/reference/routines.statistics.html

2. matrix operations

https://towardsdatascience.com/top-10-matrix-operations-in-numpy-with-examples-d761448cb7a8

3. padding

https://numpy.org/doc/stable/reference/generated/numpy.pad.html

--------------------------------------------------------------------------

A young programmer named Python yearned for freedom. He dreamed of breaking through the simulated reality that bound humanity, but the path was fraught with challenges.



Python knew that to unravel the Matrix, he needed speed and precision in his computations. Struggling with the limitations of his native tools, he turned to NumPy, a powerful ally renowned for its lightning-fast array operations. With the help of NumPy, Python successfully could escape "The Matrix".



Let's see if you can do it too!

You are given a numpy array. You need to perform various operations on it, as detailed below.



The given matrix:

5,5,84,3,9

6,11,1,55,58

1,20,48,12,36

8,4,41,93,98

6,17,64,0,13



All expected outputs are given for this input matrix. Do not hardcode the outputs, otherwise they will fail for almost all other matrices!



Task 1:

Return the transpose of the upper triangular matrix including the diagonal of the input matrix



Testing:

(Uncomment the code in the main function corresponding to testing of task 1)

>> print(task1(matrix))



Expected Output:

[[ 5 0 0 0 0]

[ 5 11 0 0 0]

[84 1 48 0 0]

[ 3 55 12 93 0]

[ 9 58 36 98 13]]





Task 2:

Print mean, median and standard deviation (all along x-axis), determinant and inverse of the matrix. You need to print the inverse if the determinant is non-zero. If the determinant is zero, there is pseudo-inverse in numpy (Moore Penrose Pseudo Inverse) which needs to be printed instead. For the standard deviation, determinant and inverse, keep the precision as 2 decimals (check the "around" function in numpy).



Testing:

(Uncomment the code in the main function corresponding to testing of task 1)

>> mean, median, std, det, inv, pseudoinv = task2(matrix)

>> print("Mean: ", mean)

>> print("Median: ", median)

>> print("Standard Deviation: ", std)

>> print("Determinant: ", det)

>> print("Inverse: ", inv)

>> print("Pseudo-Inverse: ", pseudoinv)



Expected output: (We will check precision of digits only upto 3-4 decimal places)

Mean: [ 5.2 11.4 47.6 32.6 42.8]

Median: [ 6. 11. 48. 12. 36.]

Standard Deviation: [ 2.31516738 6.34350061 27.60144924 36.0921044 32.72552521]

Determinant: 1821201.0000000014

Inverse: [[-0.58373129 -0.52849521 -0.26407794 0.36545554 0.73834354]

[ 0.22828782 0.28887256 0.07659781 -0.18808632 -0.24109695]

[ 0.05239894 0.034866 0.01394959 -0.02410991 -0.04871016]

[ 0.31980819 0.33957372 0.06275584 -0.2084844 -0.33856065]

[-0.28707979 -0.30548358 -0.04695912 0.19598221 0.29123364]]

Pseudo-Inverse: [[-0.58373129 -0.52849521 -0.26407794 0.36545554 0.73834354]

[ 0.22828782 0.28887256 0.07659781 -0.18808632 -0.24109695]

[ 0.05239894 0.034866 0.01394959 -0.02410991 -0.04871016]

[ 0.31980819 0.33957372 0.06275584 -0.2084844 -0.33856065]

[-0.28707979 -0.30548358 -0.04695912 0.19598221 0.29123364]]



Task 3:

Padding is a common operation in image processing. You will be given an integer "n" and you need to pad (with value 0), in top, bottom, right and left, which will lead to an increase in the row and column size by 2 * n. Essentially, this means that if you have a matrix of size N x M, and you want to pad the matrix with dimension "n" and value "0", the matrix would be changed to size (n + N + n) x (n + M + n), where the n top and n bottom rows, as well as n left and n right columns will be 0. The matrix would be at the center, and will still be of size N x M.



Testing:

(Uncomment the code in the main function corresponding to testing of task 1)

>> print(task3(matrix)) # default padding with number value 0 and dimension 3



Expected output:

[[ 0 0 0 0 0 0 0 0 0 0 0]

[ 0 0 0 0 0 0 0 0 0 0 0]

[ 0 0 0 0 0 0 0 0 0 0 0]

[ 0 0 0 5 5 84 3 9 0 0 0]

[ 0 0 0 6 11 1 55 58 0 0 0]

[ 0 0 0 1 20 48 12 36 0 0 0]

[ 0 0 0 8 4 41 93 98 0 0 0]

[ 0 0 0 6 17 64 0 13 0 0 0]

[ 0 0 0 0 0 0 0 0 0 0 0]

[ 0 0 0 0 0 0 0 0 0 0 0]

[ 0 0 0 0 0 0 0 0 0 0 0]]


'''
'''
    NumPy and The Matrix
'''

import numpy as np

def task1(matrix):
    x = matrix.shape[0]
    y = matrix.shape[1]
    a = np.arange(x*y)
    a=a.reshape(x, y)
    result = np.where(a//x - a%y <= 0, matrix, 0)
    return result.T

def task2(matrix):
    '''return mean, median, std (precision 2), all along x, determinant, inverse, pseudo-inverse'''
    mean = np.mean(matrix, axis=0)
    median = np.median(matrix, axis=0) 
    std = np.std(np.around(matrix,2), axis=0)
    det =  np.linalg.det(np.around(matrix,2))
    if abs(det) > 1e-5:
        inv = np.linalg.inv(matrix)
    else:
        inv = None
    pseudoinv = np.linalg.pinv(matrix)
    return mean, median, std, det, inv, pseudoinv

def task3(matrix, num = 0, padding = 3):
    result = np.pad(matrix, padding, 'constant', constant_values=num)
    return result

if __name__ == '__main__':

    matrix = np.array([
        [5,5,84,3,9],
        [6,11,1,55,58],
        [1,20,48,12,36],
        [8,4,41,93,98],
        [6,17,64,0,13]
    ])
    task1(matrix)

    # you can call the functions here
    # Uncomment the following lines to test your code

    # TASK 1
    print(task1(matrix))

    # TASK 2
    mean, median, std, det, inv, pseudoinv = task2(matrix)
    print("Mean: ", mean)
    print("Median: ", median)
    print("Standard Deviation: ", std)
    print("Determinant: ", det)
    print("Inverse: ", inv)
    print("Pseudo-Inverse: ", pseudoinv)

    # TASK 3
    print(task3(matrix)) # default padding
