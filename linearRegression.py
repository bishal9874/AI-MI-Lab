import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Read the data into a dataframe
df = pd.read_csv('/media/bishal/New Volume/AI-ML Lab Assignment/Salary_Data-2.csv')

# Split the data into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(df['YearsExperience'],df['Salary'], test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model on the training set
model.fit(X_train.values.reshape(-1, 1), y_train)

# Use the model to make predictions on the testing set
y_pred_test = model.predict(X_test.values.reshape(-1, 1))

# Plot the actual vs predicted values for the testing set
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred_test, color='red')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.title('Salary vs Experience (Testing Set)')
plt.show()

# Use the model to make predictions on the training set
y_pred_train = model.predict(X_train.values.reshape(-1, 1))

# Plot the actual vs predicted values for the training set
plt.scatter(X_train, y_train, color='blue')
plt.plot(X_train, y_pred_train, color='red')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.title('Salary vs Experience (Training Set)')
plt.show()

