'''
    Algorithm Analysis
'''
import numpy as np
from matplotlib import pyplot as plt
# common x values
X = np.arange(1,1000)
# first record 0.1nlog(n) and 0.01n^2
a = 0.1 * X * np.log(X)
b = 0.01 * X * X
# file path format string
path = 'files/data{}.txt'
# iterate through data and create the plots
for i in range(9):
  # loop for plot(i)
  print(f'Generating plot {i}')
  # perhaps you may need some variables here to store data
  for j in range(i * 3, i * 3 + 3):
    # open the files and record data
    filename=path.format(j)
    f=open(filename, "r")
    # data in 0, 3, 6.. is for QSP1
    # data in 1, 4, 7.. is for QSRP
    # data in 2, 5, 8.. is for BuSo
    data=[]
    count=0
    for k in f.readlines():
      if count%2==1:
        data.append(int(k))
      count+=1
    if j%3==0:
      QSP1=data
    elif j%3==1:
      QSRP=data
    else:
      BuSo=data
    f.close()  
  # create the plot(i)
  plt.plot(X, QSP1, color="blue", label="QSP1")
  plt.plot(X, QSRP, color="orange", label="QSRP")
  plt.plot(X, BuSo, color="green", label="BuSo")
  plt.plot(X, a, color="green", label="nlogn")
  plt.plot(X, b, color="red", label="n^2")
  # you can use if-elif-else conditions for the axes labels.
  if i<=2:
    plt.xlabel("Random Array Size")
  elif i>=3 and i<=5:
    plt.xlabel("Almost-Sorted Array Size")
  else:
    plt.xlabel("Almost-Sorted-Rev Array Size")
  if i%3==0:
    plt.ylabel("Runtime")
  elif i%3==1:
    plt.ylabel("Comparisons")
  else:
    plt.ylabel("Swaps")
  plt.legend(["QSP1", "QSRP", "BuSo", "NlogN", "N^2"], loc='upper left')
  # saving the plot
  plt.savefig(f'plots/plot{i}.png')
  plt.clf()