import pandas as pd
import numpy as np

df = pd.read_csv('data.csv', index_col = 0)

print(df)
print(df.index)
# print(df.columns[0])

#editing labels with numpy methods
df.index = np.arange(1, 8)
print(df)