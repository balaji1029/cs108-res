import numpy as np

def nonvectorized(matrix: np.ndarray):
    """
    Do not edit this function
    """
    n = matrix.shape[0]
    # Create transpose
    transpose = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            transpose[i][j] = matrix[j][i]
            
    # Element-wise multiplication
    multiplied = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            multiplied[i][j] = matrix[i][j] * transpose[i][j]

    # Matrix multiplication
    result = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix[i][k] * multiplied[k][j]
                
    return result


def vectorized(matrix: np.ndarray):
    """
    Implement the vectorized version of above nonvectorized() function. Delete the "pass" statement, write your code here and **return** the result.
    """
    return np.dot(matrix, (matrix * matrix.T))
