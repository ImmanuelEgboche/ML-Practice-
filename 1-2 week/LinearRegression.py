"""
APPROACH


- Plot the data using a scatter plot

- Compute the reggression line, calculate the slope and intercept the best fit line

- Use the regression line to make predictions

- Finally compute the mean sqaure error of the model

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = {'Size': [600, 800, 1000, 1200, 1400],
        'Price': [300000, 350000, 400000, 450000, 500000]}

df = pd.DataFrame(data)

plt.scatter(df['Size'], df['Price'])
plt.title('House Price vs Size')
plt.xlabel('Size (sq ft)')
plt.ylabel('Price ($)')
plt.show()

X = df[['Size']]  # Predictor variable
y = df['Price']   # Response variable
model = LinearRegression().fit(X, y)

# Predictions
predicted_price = model.predict([[1100], [1500]])

# Evaluate
mse = mean_squared_error(y, model.predict(X))

