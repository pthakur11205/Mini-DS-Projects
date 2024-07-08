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

#appending rows
df.loc[len(df)+1] = ['Joe', 'Boston', 45, 79.0]
print(df)

#deleting rows
df = df.drop(labels=[8])
print(df)

#appending columns
df['js-score'] = np.array([71.0, 95.0, 88.0, 79.0, 91.0, 91.0, 80.0])
print(df)
    #inserting columns
df.insert(loc=4, column='c++ score', value=np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))
print(df)

#iterating
for index, row in df.iterrows():
    print(index, row['city'])


#loc functionality
print(df.loc[df['name'] == "Xavier"])

#using desrcibe method
print(df.describe())

#sorting
# df = df.sort_values('name')
# print(df)

#adding another column with arithmetic
df['total score'] = df['js-score'] + df['py-score'] + df['c++ score']
print(df)

#deleting columns
df = df.drop(columns=['total score'])
print(df)

#new columns using iloc
#axis=1 specifies horizontal adding
df['total score'] = df.iloc[:, 3:6].sum(axis=1)
print(df)