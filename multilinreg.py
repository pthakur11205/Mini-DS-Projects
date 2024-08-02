import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = [
 [0, 1], [5, 1], [15, 2], 
 [25, 5], [35, 11], [45, 15], 
 [55, 34], [60, 35]
 ]

y = [4, 5, 20, 14, 32, 22, 38, 43]

plt.plot(x, y)
plt.show()