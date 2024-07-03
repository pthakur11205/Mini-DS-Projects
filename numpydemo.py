import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

a = np.arange(10)**3
print(a)

#slicing
print(a[2:5])
print(a[:4])
print(a[-6:])

a = np.arange(12).reshape(3, 4)
print(a)

#splitting a into 2
b = np.hsplit(a, 2)
print(b)


#check dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim) #0
print(b.ndim) #1
print(c.ndim) #2
print(d.ndim) #3

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()