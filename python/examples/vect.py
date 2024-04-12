import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i in range(len(x)):
    z.append(x[i] + y[i])

w = np.add(x, y)

print("array x:", x)
print("array y:", y)
print("array z:", z)
print("array w:", w)
print("z type:", type(z))
print("w type:", type(w))

a = np.array([1, 2, 3, 4])
b = np.array([3, 0, 1, 2])

c = a + b
print("array c:", c)
