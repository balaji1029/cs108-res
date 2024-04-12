import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("array a:", a)

b = a.reshape(4, 3)
print("array b:", b)

c = a.reshape(2, 3, 2)
print("array c:", c)

d = a.reshape(2, -1, 3)
print("array d:", d)