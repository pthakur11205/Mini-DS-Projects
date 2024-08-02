import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

model = LinearRegression()
model.fit(x, y)

#Calculate R^2 and display
r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")
print(f"The x explains {(r_sq*100).round(2)}% of y's variation")

#Print slope and intercept of equation
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")