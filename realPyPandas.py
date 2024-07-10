import pandas as pd
import numpy as np

data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai', 'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

row_labels = [101, 102, 103, 104, 105, 106, 107]

#creating data frame
df = pd.DataFrame(data=data, index = row_labels)
print(df)

print(df['age'])
print(df.age[104])

print(' ')

arr = np.array([
[1, 3, 5],
[2, 4, 6],
[3, 5, 7]
])


df = pd.DataFrame(arr, columns = ['num1', 'num2', 'num3'], 
                  index=[1, 2, 3], copy = True)

#testing copy function
#when copy is true, modifications are not in dataframe
#when copy is false (default), mods ARE in data frame
arr[0, 0] = 1000

print(df)

#concat testing
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)

df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)

result = pd.concat([df1, df2, df3])

print(result)

#join specifies how to handles values that dont exist in the first df
    #join = outer takes union of axis values
df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)

result = pd.concat([df1, df4], axis=1)

print(result)

    #join = inner takes intersection of axis values
result = pd.concat([df1, df4], axis=1, join="inner")
print(result)

#reindexing
result = pd.concat([df1, df4], axis=1).reindex(df1.index)
print(result)

#concat series as column and df together
s1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")

result = pd.concat([df1, s1], axis = 1)
print(result)

#concat series as row and df together
    #convert series to a dataframe then concat
s1 = pd.Series(["X0", "X1", "X2", "X3"], index=["A", "B", "C", "D"])

result = pd.concat([df1, s1.to_frame().T], ignore_index=True)
print(result)

#using keys as identifiers for separate dataframes
result = pd.concat([df1, df2, df3], keys = ["a", "b", "c"])
print(result)

print(result.loc["c"])

#merge() has different operations
    # one-to-one: joining two DataFrame objects on their indexes which must contain unique values.

    # many-to-one: joining a unique index to one or more columns in a different DataFrame.

    # many-to-many : joining columns on columns.


