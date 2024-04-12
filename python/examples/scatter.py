import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.randint(100, size=20)
y1 = np.random.randint(100, size=20)

x2 = np.random.randint(100, size=20)
y2 = np.random.randint(100, size=20)

plt.scatter(x1, y1, c='magenta', alpha=0.8, marker='*', s=50, label='Class 1')
plt.scatter(x2, y2, c='cyan', alpha=0.7, marker='D', s=50, label='Class 2')

plt.title('Scatter Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()

plt.savefig('scatter.png')
