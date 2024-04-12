import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'red')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = 'green')

plt.show() 

#Another interesting example of scatterplot
#100 random values in x, y arrays
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
#colors,sizes is also an array with random values
colors = np.random.randint(100, size=(100))
#sizes also is random
sizes = np.random.randint(100, size=(100))
#adjust the transparency of the dots with the alpha argument.
#cmap is an in-built colormap, you can also try 'viridis' as cmap
plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='nipy_spectral')

#plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')

#A colormap is like a list of colors, where each color has a value that ranges from 0 to 100. 
#colorbar shows this.
plt.colorbar()

plt.show() 

#Bar plot

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = 'r', width = 0.5)
plt.show()

#pie chart
#The size of each wedge is determined by comparing the value with all the other values, by using this formula: y/sum(y)
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

#math functions
x= np.arange(-2*np.pi, 2*np.pi, 0.1)
plt.plot(x, np.sin(x), label='sine')
plt.plot(x, np.cos(x), label = 'cosine')
plt.legend()
#save the plot to a file, can choose jpg, png etc also
plt.savefig('math.pdf')
plt.show()


