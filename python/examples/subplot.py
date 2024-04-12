import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 400)
y0 = np.sin(x)
plt.subplot(2, 2, 1)
plt.plot(x, y0, c = 'r')
plt.title('Sine curve')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

y1 = np.cos(x)
plt.subplot(2, 2, 2)
plt.plot(x, y1, c = 'g')
plt.title('Cosine curve')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

y2 = np.tan(x)
plt.subplot(2, 2, 3)
plt.plot(x, y2, c = 'b')
plt.title('Tangent curve')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

y3 = np.exp(x)
plt.subplot(2, 2, 4)
plt.plot(x, y3, c = 'y')
plt.title('Exponential curve')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.suptitle('Different types of curves')
plt.tight_layout()
plt.show()