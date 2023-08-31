import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the CSV file into a pandas dataframe
df = pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/python/Housing data.csv")  # Update with the correct file path

# Split the data into features and labels
X = df.drop('Sales price', axis=1)
y = df['Sales price']

# Create a Linear Regression object
reg = LinearRegression()

# Train the model on the data
reg.fit(X, y)

# Get input features from user
new_house = {}
for feature in X.columns:
    new_value = float(input(f'Enter {feature}: '))  # Convert input to float
    new_house[feature] = new_value

# Create a DataFrame for the new house
new_house_df = pd.DataFrame([new_house])

# Ensure input features match the model's feature order
new_house_features = new_house_df[X.columns]

# Predict the price of the new house based on input features
prediction = reg.predict(new_house_features)

# Print out the prediction
print(f'The predicted price of the new house is ${prediction[0]:,.2f}.')
