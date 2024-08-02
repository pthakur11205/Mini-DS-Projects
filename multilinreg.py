import numpy as np
from sklearn.linear_model import LinearRegression

x = [
 [0, 1], [5, 1], [15, 2], 
 [25, 5], [35, 11], [45, 15], 
 [55, 34], [60, 35]
 ]

y = [4, 5, 20, 14, 32, 22, 38, 43]

#Create model
model = LinearRegression().fit(x, y)

#Print properties of model
print(model.score(x, y))
print(model.intercept_)
print(model.coef_)

#Predictions
model_preds = model.predict(x)
print(model_preds)