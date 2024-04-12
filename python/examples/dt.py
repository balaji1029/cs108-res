import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array(["apple", "banana", "cherry"])

print("array a:", a)    
print("a dtype:", a.dtype)
print("array b:", b)
print("b dtype:", b.dtype)

c = np.array([12, 21, 32, 40], dtype='S')
print("array c:", c)
print("c dtype:", c.dtype)

d = np.array([1, 2, 3, 4], dtype='f')
print("array d:", d)
print("d dtype:", d.dtype)

e = np.array([1.2, 2.3, 3.4], dtype='float32')
print("e dtype:", e.dtype)
f = e.astype('i')
print("array f:", f)
print("f dtype:", f.dtype)

g = np.array([1, 0, 3, 0, 5])
print("g dtype:", g.dtype)
h = g.astype(bool)
print("array h:", h)
print("h dtype:", h.dtype)