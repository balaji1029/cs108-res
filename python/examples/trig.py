import numpy as np

a = np.array([[0, np.pi/6], [np.pi/4, np.pi/3]])
print("array a:", a)
b = np.sin(a)
print("array b:", b)
c = np.cos(a)
print("array c:", c)
d = np.tan(a)
print("array d:", d)

e = np.array([[0, 30], [45, 60]])
print("array e:", e)
f = np.radians(e)
print("array f:", f)
g = np.degrees(f)
print("array g:", g)