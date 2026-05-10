from sklearn.linear_model import LinearRegression
import numpy as np

# বাড়ির size (বর্গফুট)
size = np.array([500, 750, 1000, 1250, 1500]).reshape(-1, 1)

# বাড়ির price (লক্ষ টাকা)
price = np.array([20, 30, 40, 50, 60])

# Model বানাও
model = LinearRegression()
model.fit(size, price)

# 1100 বর্গফুটের বাড়ির price কত?
prediction = model.predict([[1100]])
print("1100 sqft house price:", round(prediction[0], 2), "lak taka ")