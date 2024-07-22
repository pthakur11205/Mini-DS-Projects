import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

x = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]
# print(x)
# print(x_with_nan)

y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
# print(y)
# print(y_with_nan)
# print(z)
# print(z_with_nan)

mean = statistics.mean(x)
print(mean)

#nan values return a NaN mean
mean = statistics.mean(x_with_nan)
print(mean)

#pandas can bypass this since parameter skipna
mean = z_with_nan.mean()
print(mean)

#weighted mean demo
x = [8.0, 1, 2.5, 4, 28.0]
w = [0.1, 0.2, 0.3, 0.25, 0.15]
wmean = sum(w[i] * x[i] for i in range(len(x))) / sum(w)
print(wmean)
wmean = np.average(y, weights=w)
print(wmean)
