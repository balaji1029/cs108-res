'''
    NumPy and The Matrix
'''

from argparse import ArgumentParser as ap
import numpy as np

def task1(matrix):
    '''print the upper diagonal matrix in column-wise fashion'''
    n=np.size(matrix[0])
    datanew=matrix.T
    for i in range(0, n):
      for j in range(0, i+1):
        if j != i:
          print(datanew[i][j], end=' ')
        else:
          print(datanew[i][j])

def task2(matrix):
    '''print mean, median, std (precision 2), all along x, determinant and inverse/pseudo-inverse'''
    print(np.mean(matrix, axis=0))
    print(np.median(matrix, axis=0))
    std=np.std(matrix, axis=0)
    np.set_printoptions(suppress=True, precision=2)
    print(std)
    det=np.linalg.det(matrix)
    if det != 0:
      print(np.linalg.inv(matrix))
    else:
      print(np.linalg.pinv(matrix))
    
def task3(matrix):
    '''print after sorting along vertical and horizontal and then print flattened array'''
    print(np.sort(matrix, axis=0))
    print(np.sort(matrix, axis=1))
    print(np.sort(matrix.reshape(-1)))

def task4(matrix):
    '''print the unique frequencies of the sorted array and the frequency of second-largest'''
    new=np.sort(matrix.reshape(-1))
    print(new)
    dict={}
    for i in new:
      if i not in dict.keys():
        dict.update({i:0})
      dict[i]+=1
    listmy=list(dict.values())
    print(np.asarray(listmy))
    print(listmy[-2])
    
def task5(matrix, num = 0):
    '''print the padded matrix'''
    print(np.pad(matrix, num, mode="constant"))
if __name__ == '__main__':

    parser = ap()
    parser.add_argument('--path',type=str,required=True)
    parser.add_argument('--num',type=str,required=False)
    args = parser.parse_args()
    
    # converting csv to numpy
    data = np.genfromtxt(args.path,delimiter=',',dtype=int)

    # you can call the functions here
    # example call
    task4(data)
    # task1(data)
