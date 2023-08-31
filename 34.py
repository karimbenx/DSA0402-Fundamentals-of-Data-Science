import pandas as pd
import numpy as np

# Define the distance function (Euclidean distance)
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

# Load the patient data into a pandas dataframe
df = pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/patientdata.csv")

# Split the data into features and labels
X = df.drop('outcome', axis=1).values
y = df['outcome'].values

# Split the data into training and testing sets
split_ratio = 0.2
split_idx = int(split_ratio * len(X))
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

# Define the number of neighbors (k)
k = 3

# Function to predict the class label for a new instance
def predict_class(X_train, y_train, new_instance, k):
    distances = [euclidean_distance(new_instance, x) for x in X_train]
    sorted_indices = np.argsort(distances)
    k_nearest_indices = sorted_indices[:k]
    k_nearest_labels = y_train[k_nearest_indices]
    unique_labels, counts = np.unique(k_nearest_labels, return_counts=True)
    predicted_label = unique_labels[np.argmax(counts)]
    return predicted_label

# Make predictions on the test data
y_pred = [predict_class(X_train, y_train, x, k) for x in X_test]

# Calculate evaluation metrics for the model's predictions on the test data
def calculate_metrics(actual, predicted, positive_class):
    accuracy = np.mean(actual == predicted)
    true_positives = np.sum((actual == positive_class) & (predicted == positive_class))
    false_positives = np.sum((actual != positive_class) & (predicted == positive_class))
    false_negatives = np.sum((actual == positive_class) & (predicted != positive_class))
    
    if true_positives == 0:
        precision = 0.0
        recall = 0.0
    else:
        precision = true_positives / (true_positives + false_positives)
        recall = true_positives / (true_positives + false_negatives)
    
    if precision == 0.0 or recall == 0.0:
        f1 = 0.0
    else:
        f1 = 2 * (precision * recall) / (precision + recall)
    
    return accuracy, precision, recall, f1

positive_class = 'Positive'  # Adjust this based on your actual class labels

accuracy, precision, recall, f1 = calculate_metrics(y_test, y_pred, positive_class)

# Print out the evaluation metrics
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1-score: {f1:.2f}')
