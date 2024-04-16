# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample data
X = np.array([[1], [2], [3], [4], [5]])  # Input feature
y = np.array([2, 4, 5, 4, 5])            # Target variable

# Creating a linear regression model
model = LinearRegression()

# Training the model
model.fit(X, y)

# Making predictions
X_test = np.array([[6], [7]])  # New data for prediction
predictions = model.predict(X_test)

# Evaluating the model
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Visualizing the results
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, model.predict(X), color='red', label='Linear regression line')
plt.scatter(X_test, predictions, color='green', label='Predictions')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()
