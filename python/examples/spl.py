import numpy as np

a = np.ones((2, 3))
print("array a:", a)

b = np.zeros((4, 2))
print("array b:", b)

c = np.full((2, 2), 7)
print("array c:", c)

d = np.eye(3)
print("array d:", d)

e = np.diag(np.array([1, 2, 3, 4]))
print("array e:", e)

f = np.arange(10)
print("array f:", f)

g = np.random.randint(10, size=(2, 2))
print("array g:", g)

h = np.random.rand(2, 2)
print("array h:", h)