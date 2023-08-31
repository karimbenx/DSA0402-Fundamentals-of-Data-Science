import pandas as pd
import numpy as np

# Load transaction data into a pandas dataframe
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'amount_spent': [100, 50, 300, 200, 150, 250, 80, 120, 400, 350],
    'visit_frequency': [5, 3, 8, 6, 4, 7, 2, 3, 9, 8]
}

df = pd.DataFrame(data)

# Normalize the data
df['amount_spent'] = (df['amount_spent'] - df['amount_spent'].mean()) / df['amount_spent'].std()
df['visit_frequency'] = (df['visit_frequency'] - df['visit_frequency'].mean()) / df['visit_frequency'].std()

# Set the number of clusters
num_clusters = 3

# Initialize centroids randomly
centroids = df.sample(num_clusters)

# Perform K-Means clustering
for _ in range(10):  # Number of iterations
    # Calculate distances to centroids
    distances = np.sqrt(((df[['amount_spent', 'visit_frequency']].values[:, np.newaxis, :] - centroids[['amount_spent', 'visit_frequency']].values[np.newaxis, :, :])**2).sum(axis=2))
    
    # Assign data points to the nearest cluster
    cluster_assignments = np.argmin(distances, axis=1)
    
    # Update centroids
    for i in range(num_clusters):
        cluster_data = df[cluster_assignments == i][['amount_spent', 'visit_frequency']]
        centroids.loc[i] = cluster_data.mean()  # Use .loc to update centroids

# Add cluster assignments to the dataframe
df['cluster'] = cluster_assignments

# Print the resulting clusters
for cluster_num in range(num_clusters):
    cluster_data = df[df['cluster'] == cluster_num]
    print(f"Cluster {cluster_num}:\n{cluster_data}\n")
