import pandas as pd
from sklearn.cluster import KMeans

# Load the CSV file into a pandas dataframe
df = pd.read_csv('C:/Users/Merwin S/OneDrive/Desktop/Customer_reviews.csv')

# Split the data into features
X = df.drop('customer_id', axis=1)

# Create a KMeans clustering object with k clusters
k=5
kmeans = KMeans(n_clusters=k)

# Fit the clustering model to the data
kmeans.fit(X)

# Get input features from user
new_customer = []
for feature in X.columns:
    new_value = input(f'Enter {feature}: ')
    new_customer.append(new_value)

# Assign the new customer to one of the existing segments based on input features
prediction = kmeans.predict([new_customer])

# Print out the prediction
print(f'The new customer is assigned to segment {prediction[0]}.')
