import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(60, 8, 10000)

plt.hist(x, bins=20, color='hotpink', edgecolor='black', label='marks')
plt.title('Histogram of marks')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.show()