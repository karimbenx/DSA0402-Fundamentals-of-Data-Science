import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load the CSV file into a pandas dataframe
df = pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/churn.csv")  # Update with the correct file path

# Split the data into features and labels
X = df.drop('churn', axis=1)
y = df['churn']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create a Logistic Regression object
logreg = LogisticRegression()

# Train the model on the training data
logreg.fit(X_train_scaled, y_train)

# Get input features from user
new_customer = {}
for feature in X.columns:
    new_value = float(input(f'Enter {feature}: '))  # Convert input to float
    new_customer[feature] = new_value

# Create a DataFrame for the new customer
new_customer_df = pd.DataFrame([new_customer])

# Scale the features for the new customer
new_customer_scaled = scaler.transform(new_customer_df)

# Predict whether the new customer will churn or not
prediction = logreg.predict(new_customer_scaled)

if prediction[0] == 0:
    churn_status = "not churned"
else:
    churn_status = "churned"

# Print out the prediction
print(f'The new customer is predicted to be {churn_status}.')
