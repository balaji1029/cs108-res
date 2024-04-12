import matplotlib.pyplot as plt
import numpy as np

x = np.array([4, 7, 8, 10])
y = np.array([2, 14, 10, 16])

plt.plot(x, y, marker = '*', ls = ':', lw = 2, c = 'r', ms = 10, mec = 'g', mfc = 'hotpink')
plt.title('Line Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(axis='y', color='b', ls='--', lw=1)
plt.show()
