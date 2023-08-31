import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load the car data into a pandas dataframe
df = pd.read_csv ("C:/Users/Merwin S/OneDrive/Desktop/cardata.csv")

# Select the features to use for linear regression
features = ['engine_size', 'horsepower', 'fuel efficiency']

# Build a linear regression model to predict car prices based on the selected features
X = df[features]
y = df['price']
reg = LinearRegression()
reg.fit(X, y)

# Evaluate the model's performance using R-squared score
y_pred = reg.predict(X)
r2 = r2_score(y, y_pred)
print(f'R-squared score: {r2:.2f}')

# Analyze the model's coefficients to identify the most influential factors affecting car prices
coefficients = pd.DataFrame({'feature': features, 'coefficient': reg.coef_})
coefficients = coefficients.sort_values('coefficient', ascending=False)
print(coefficients)
