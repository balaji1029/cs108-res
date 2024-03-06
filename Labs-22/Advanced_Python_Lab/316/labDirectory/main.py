'''
    Distributions
'''

import numpy as np
from matplotlib import pyplot as plt

# take samples from each of the distributions and plot the sub-plot histogram
# use the numpy random library

#Beta
sample=np.random.beta(4,20,10000)*100
plt.subplot(3, 2, 1)
plt.hist(sample, bins=np.arange(-5, 51, 1))
plt.title("Beta")

#Exponential
sample=np.random.exponential(0.1, 10000)*100
plt.subplot(3, 2, 2)
plt.hist(sample, bins=np.arange(-1, 51, 1))
plt.title("Exponential")

#Gamma
sample=np.random.gamma(2, 0.1, 10000)*100
plt.subplot(3, 2, 3)
plt.hist(sample, bins=np.arange(-1, 51, 1))
plt.title("Gamma")

#Laplace
sample=np.random.laplace(0, 0.5, 10000)*100
plt.subplot(3, 2, 4)
plt.hist(sample, bins=np.arange(-1, 51, 1))
plt.title("Laplace")

#Normal
sample=np.random.normal(0, 3, 10000)
plt.subplot(3, 2, 5)
plt.hist(sample, bins=np.arange(-10, 12, 1))
plt.title("Normal")

#Poisson
sample=np.random.poisson(3, 10000)
plt.subplot(3, 2, 6)
plt.hist(sample, bins=np.arange(-1, 12, 1))
plt.title("Poisson")

# save your plot in the end
plt.savefig('plot.png')
