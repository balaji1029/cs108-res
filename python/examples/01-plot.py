import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
#The below plot() function is used to draw points (markers) in a diagram
#Marker can be '*', '.', '+', 'D' (diamond), 'p' (pentagon) etc also
plt.plot(xpoints, ypoints, marker = 'o')
plt.show()

#marker|line|color (e.g. o:r), o is marker, : is line and r is red; no need to mention marker here
plt.plot(xpoints, ypoints,'o:r')
plt.show()

#mec: marker edge color, ms: marker size: ls: linestyle, mfc: marker face color
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'g', ls = '-.', mfc = 'hotpink')
plt.show()

#multiple plots
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
# Function add a legend  
plt.legend(["plot1", "plot2"], loc ="lower right")
plt.show()

