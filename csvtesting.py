import pandas as pd
import numpy as np

df = pd.read_csv('data.csv', index_col = 0)

print(df)
print(df.index)
# print(df.columns[0])

#editing labels with numpy methods
df.index = np.arange(1, 8)
print(df)

#to get unlabeled data as numpy array, use .to_numpy() or .values
arrData = df.values
print(arrData)

#accessing data
print(df.city)
print(df.loc[2])

#.loc and .iloc function with slicing and column specification
print(df.loc[1:4, ['name', 'age']])
print(df.iloc[0:4, [0, 2]])

#at and iat
print(df.at[1, 'name'])
print(df.iat[0, 0])