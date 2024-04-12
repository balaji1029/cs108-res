import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [1, 2]])
print("array a:", a)
print("array b:", b)

c = np.multiply(a, b)
print("array c:", c)
e = np.matmul(a, b)
print("array e:", e)
f = a @ b
print("array f:", f)

g = np.transpose(a)
print("array g:", g)
h = a.T
print("array h:", h)

i = np.linalg.inv(a)
print("array i:", i)

j = np.linalg.det(a)
print("array j:", j)