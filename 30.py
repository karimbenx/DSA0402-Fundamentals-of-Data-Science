import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Load the CSV file into a pandas dataframe
df = pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/car_data.csv")

# Split the data into features and labels
X = df.drop('price', axis=1)
y = df['price']

# Create a Decision Tree Regressor object
reg = DecisionTreeRegressor()

# Train the model on the data
reg.fit(X, y)

# Get input features from user
new_car = []
for feature in X.columns:
    new_value = input(f'Enter {feature}: ')
    new_car.append(new_value)

# Predict the price of the new car based on input features
prediction = reg.predict([new_car])

# Print out the predicted price and decision path for the new car
print(f'The predicted price of the new car is ${prediction[0]:,.2f}.')
path = reg.decision_path([new_car])
print(f'The decision path for the new car is {path}.')
