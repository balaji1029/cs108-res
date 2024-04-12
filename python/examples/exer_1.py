import numpy as np
import time 

def py_list(dim):
    matrix = [[dim*i+j for j in range(dim)] for i in range(dim)]
    square = [[0 for j in range(dim)] for i in range(dim)]
    start = time.time()
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                square[i][j] += matrix[i][k] * matrix[k][j] 
    end = time.time()
    print(f'Python list elapsed time: {end-start} seconds')

def np_array(dim):
    matrix = np.arange(dim*dim).reshape(dim, -1)
    start = time.time()
    square = matrix @ matrix
    end = time.time()
    print(f'NumPy array elapsed time: {end-start} seconds')

if __name__ == '__main__':
    dim = 1000
    py_list(dim)
    np_array(dim)