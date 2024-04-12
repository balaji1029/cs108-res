import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#loc specifies location: left, center or right
#fontdict parameter to set font properties
plt.title("Sports Watch Data", fontdict = font1, loc = 'left')
plt.xlabel("Average Pulse", fontdict =  font2)
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.plot(x, y)

#adds a grid, c: color, ls: line style, lw: line width
#plt.grid(c = 'g', ls = '--', lw = 0.5)
# can also specify axis via axis option; comment above line and uncomment below line and see
plt.grid(axis = 'y')
plt.show()

