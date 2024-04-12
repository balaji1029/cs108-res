import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
b = [True, False, True, False, True, False]
c = a[b]
print("array c:", c)

d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
e = [[True, False, True, False], [False, False, False, True]]
f = d[e]
print("array f:", f)