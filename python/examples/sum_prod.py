import numpy as np

a = np.array([[[1, 2], [3, 4]], [[5, 6], [1, 2]]])
print("array a:", a)

b = np.sum(a)
print("array b:", b)
c = np.sum(a, axis=0)
print("array c:", c)
d = np.sum(a, axis=1)
print("array d:", d)
e = np.sum(a, axis=2)
print("array e:", e)

f = np.prod(a)
print("array f:", f)
g = np.prod(a, axis=0)
print("array g:", g)
h = np.prod(a, axis=1)
print("array h:", h)
i = np.prod(a, axis=2)
print("array i:", i)
