'''
    NumPy and The Matrix
'''

from argparse import ArgumentParser as ap
import numpy as np

def task1(matrix):
    '''print the upper diagonal matrix in column-wise fashion'''
    

def task2(matrix):
    '''print mean, median, std (precision 2), all along x, determinant and inverse/pseudo-inverse'''
    

def task3(matrix):
    '''print after sorting along vertical and horizontal and then print flattened array'''
    

def task4(matrix):
    '''print the unique frequencies of the sorted array and the frequency of second-largest'''
    

def task5(matrix, num = 0):
    '''print the padded matrix'''
    

if __name__ == '__main__':

    parser = ap()
    parser.add_argument('--path',type=str,required=True)
    parser.add_argument('--num',type=str,required=False)
    args = parser.parse_args()

    # converting csv to numpy
    data = np.genfromtxt(args.path,delimiter=',',dtype=int)

    # you can call the functions here
    # example call
    # task1(data)
