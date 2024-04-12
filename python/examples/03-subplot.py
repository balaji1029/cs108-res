import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

#subplot specfies, rows and columnns in the figure and position of this subplot
#Create a 1x2 grid of subplots and select the first subplot --> (1,2,1)
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

#Super title for the entire fig
plt.suptitle("MY SHOP")
plt.show()

#Another example with many subplots
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

#Create a 2x3 grid of subplots and select the first subplot
plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([2, 4, 5, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 15, 25, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 0, 6, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 12, 8, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()

