import numpy as np

a = np.array([1, 2, 3, 4, 5])
c = a.copy()
a[0] = 42

print(a)
print(c)

v = a.view()
a[0] = 10
v[4] = 40

print(a)
print(v)
print(c)