import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the CSV file into a pandas dataframe
df = pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/clinical_trial_data.csv")

# Get input features and target variable from user
X_cols = input('Enter the names of the input features separated by commas: ').split(',')
y_col = input('Enter the name of the target variable: ')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[X_cols], df[y_col], test_size=0.2)

# Create a Logistic Regression object
clf = LogisticRegression()

# Train the model on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate evaluation metrics for the model's predictions on the test data
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Print out the evaluation metrics
print(f'Accuracy: {accuracy:.2%}')
print(f'Precision: {precision:.2%}')
print(f'Recall: {recall:.2%}')
print(f'F1-score: {f1:.2%}')

