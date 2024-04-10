'''
    Distributions
'''

import numpy as np
from matplotlib import pyplot as plt

# Seeding for reproducibility
np.random.seed(101)

# sampling from each of the six distributions
beta_list = np.random.beta(4,20,1000000)
exponential_list = np.random.exponential(0.1,1000000)
gamma_list = np.random.gamma(2,0.1,1000000)
laplace_list = np.random.laplace(0,0.5,1000000)
poisson_list = np.random.poisson(3,1000000)
normal_list = np.random.normal(0,3,1000000)


# plotting histograms for each of the distributions
fig, axes = plt.subplots(3,2)
axes[0,0].hist(100*beta_list, bins=55, range=(-5,50), color='r')
axes[0,0].set_title('Beta')
axes[0,1].hist(100*exponential_list, bins=51, range=(-1,51), color='g', alpha=0.5)
axes[0,1].set_title('Exponential')
axes[1,0].hist(100*gamma_list, bins=51, range=(-1,51),alpha=0.8,orientation='horizontal',color='black')
axes[1,0].set_title('Gamma')
axes[1,1].hist(100*laplace_list,histtype='bar',bins=51, range=(-1,50),color='orange')
axes[1,1].set_title('Laplace')
axes[2,0].hist(normal_list,bins=21,range=(-10,11))
axes[2,0].set_title('Normal')
axes[2,1].hist(poisson_list,bins=12,range=(-1,11))
# adjust the sub-plots to fit the titles and labels
plt.tight_layout()
# save the plot as plot.png
plt.savefig('plot.png')
# plt.show()
