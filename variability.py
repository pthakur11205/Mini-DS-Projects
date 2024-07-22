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