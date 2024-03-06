'''
    Algorithm Analysis
'''
import numpy as np
from matplotlib import pyplot as plt
# common x values

# first record 0.1nlog(n) and 0.01n^2

# file path format string
path = 'files/data{}.txt'
# iterate through data and create the plots

  # loop for plot(i)
  print(f'Generating plot {i}')
  # perhaps you may need some variables here to store data

    # open the files and record data

    # data in 0, 3, 6.. is for QSP1
    # data in 1, 4, 7.. is for QSRP
    # data in 2, 5, 8.. is for BuSo

  # create the plot(i)

  # you can use if-elif-else conditions for the axes labels.

  # saving the plot
  plt.savefig(f'plots/plot{i}.png')
  plt.clf()
