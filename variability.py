import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

x = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]

#mean
print(statistics.mean(x))

#sample variance
print(statistics.variance(x))

#std
print(statistics.stdev(x))

#skewness
y = np.array(x)
print(scipy.stats.skew(y, bias=False))
z = pd.Series(x)
print(z.skew())

#percentiles
x = [-5.0, -1.1, 0.1, 2.0, 8.0, 12.8, 21.0, 25.8, 41.0]
print(statistics.quantiles(x, n=2))

print(z.describe())

#covariance
cov_matrix = np.cov(x, y)
print(cov_matrix)