import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Load the CSV file into a pandas dataframe
df = pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/Patient_data.csv")  # Update with the correct file path

# Split the data into features and labels
X = df.drop('condition', axis=1)
y = df['condition']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Get input features from user
new_patient = {}
for feature in X.columns:
    new_value = float(input(f'Enter {feature}: '))  # Convert input to float
    new_patient[feature] = new_value

# Create a DataFrame for the new patient
new_patient_df = pd.DataFrame([new_patient])

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
new_patient_scaled = scaler.transform(new_patient_df)

# Get input for the number of neighbors (k)
k = int(input("Enter the number of neighbors (k): "))

# Create a KNN Classifier object
knn = KNeighborsClassifier(n_neighbors=k)

# Train the model on the training data
knn.fit(X_train_scaled, y_train)

# Predict whether the new patient has the medical condition or not
prediction = knn.predict(new_patient_scaled)

# Print out the prediction
if prediction[0] == 0:
    condition = "no serious"
else:
    condition = "serious"

print(f'The new patient is predicted to have {condition}.')
