import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load the house data into a pandas dataframe
df = pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/house_data.csv")

# Select the feature to use for bivariate analysis and linear regression
feature = 'size'

# Perform bivariate analysis to visualize the relationship between the selected feature and house prices
import matplotlib.pyplot as plt
plt.scatter(df[feature], df['price'])
plt.title('Bivariate Analysis')
plt.xlabel(feature)
plt.ylabel('Price')
plt.show()

# Build a linear regression model to predict house prices based on the selected feature
X = df[[feature]]
y = df['price']
reg = LinearRegression()
reg.fit(X, y)

# Evaluate the model's performance using R-squared score
y_pred = reg.predict(X)
r2 = r2_score(y, y_pred)
print(f'R-squared score: {r2:.2f}')
