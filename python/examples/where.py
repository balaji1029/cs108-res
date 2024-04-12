import numpy as np

a = np.array([1, 2, 3, 4, 5, 4, 4])
b = np.where(a == 4)
print("array b:", b)
c = np.where(a % 2 == 0)
print("array c:", c)