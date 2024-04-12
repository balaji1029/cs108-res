import numpy as np

a = np.array([1, 2, 3, 4])
b = 5
print("array a:", a)
print("scalar b:", b)
c = a + b
print("array c:", c)

d = np.ones((8, 1, 6, 1))
print("shape of d:", d.shape)
e = np.ones((7, 1, 5)) 
print("shape of e:", e.shape)
f = d + e
print("shape of f:", f.shape)

g = np.array([[1, 2, 3, 4]]).T
h = np.array([[1, 0, 1, 2], [2, 1, 0, 3], [3, 2, 1, 4], [4, 3, 2, 5]])
print("array g:", g)
print("array h:", h)
print("shape of g:", g.shape)
print("shape of h:", h.shape)
i = g * h
print("array i:", i)
print("shape of i:", i.shape)
