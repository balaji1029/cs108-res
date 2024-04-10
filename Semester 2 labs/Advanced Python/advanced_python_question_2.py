'''
Distributions
--------------------------------------------------------------------------

References/Links



1. https://numpy.org/doc/stable/reference/random/legacy.html



2. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html



3. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html (Check **kwargs for blending factor)



5. https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html

--------------------------------------------------------------------------



NumPy is also used widely for the various and commonly occurring mathematical and probabilistic distributions and sampling. Combined with PyPlot from Matplotlib, they give a good API for data analysis and interpretation.



Your task would be to sample each of the below six distributions S=1000000 times and then plot the frequency histograms for these samples. You need to create a single figure that has 6 subplots which should be arranged as 1, 2 in the first row, 3, 4 in second row and 5 and 6 in the third row (so 3x2 sub-plot).



For sampling each of them, the input size should be set to S. Larger the sample size, better the estimation of the distribution. You can go through the documentation reference (provided in the links) to find the appropriate parameter to set in the numpy functions.



Some clarifications for the terminology used below:

1. The parameters (a, b, scale, loc, etc) all refer to the statistical variables that are used to adjust the shape of the distributions (check the documentation and the formulae for them for more details as all these distributions are used very commonly)

2. The "values" are the outputs obtained from the distributions, so there will be S values for each of the distributions, and you need to scale them as indicated(by scaling we mean, multiplying by the factor as mentioned)

3. The "range" and "step" are both for the x-axis of the plots, and indicate the range of input, so the histogram will essentially tell you how many of the samples fell in which range

4. Apart from this we also mention the visual appeal of each of the subplots. Read through documentation to figure out how to achieve these.

5. Every subplot needs to have a title corresponding to the distribution being plotted as a histogram.



(1) Beta. a = 4, b = 20. Multiply the values by 100. Range -5 to 50. Step 1. Color of histogram is red. Title = "Beta"



(2) Exponential. scale = 0.1. Multiply the values by 100. Range -1 to 50. Step 1. Color of histogram is green with 0.5 blending factor. Title = "Exponential"



(3) Gamma. scale = 0.1, shape = 2. Multiply the values by 100. Range -1 to 50. Step 1. Color of histogram is black with blending factor of 0.8 but orientation is horizontal. Title = "Gamma"



(4) Laplace. scale = 0.5, loc = 0. Multiply the values by 100. Range -1 to 50. Step 1. Color is orange. Title = "Laplace"



(5) Normal (Gaussian). loc = 0, scale = 3. Range -10 to 11. Step 1. Default color. Title = "Normal"



(6) Poisson. lam = 3. Range -1 to 11. Step 1. Default color. Title = "Poisson"



Expected output for this is given as expected_plot.png



NOTE:

You may notice, that the autograder is stochastic and possibly may give different marks on different runs. To make this deterministic, set a seed before you do the sampling from distributions.
Autograder may not be always correct. It may give you full score even when partially correct. You need to verify your generated plot.png by comparing against expected_plot.png.
'''
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
