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
                  index=[1, 2, 3])

print(df)