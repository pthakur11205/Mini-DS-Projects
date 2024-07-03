import numpy as np

a = np.array([2, 3, 4])
b = np.array([1.2, 3.5, 5.1])
print(a.dtype)
print(b.dtype)

# a = np.arange(15).reshape(5, 3)

# print(a)

#Basic arithmetic
c = a - b
print(c)
c = a * b
print(c)