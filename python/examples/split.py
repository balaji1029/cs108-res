import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array_split(a, 3)
print("array b:", b)
c  = np.array_split(a, 4)
print("array c:", c)

d = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
e = np.array_split(d, 2)
print("array e:", e)
f = np.array_split(d, 2, axis=1)
print("array f:", f)

g = np.hsplit(d, 2)
print("array g:", g)
h = np.vsplit(d, 3)
print("array h:", h)