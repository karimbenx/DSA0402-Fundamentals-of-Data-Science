import pandas as pd
import numpy as np

# Load customer data into a pandas dataframe
data = {
    'purchase_history': [5, 2, 10, 8, 12, 4, 6, 9, 1, 11],
    'browsing_behavior': [10, 2, 8, 7, 3, 9, 6, 1, 11, 4],
    'demographics': [25, 40, 30, 28, 22, 35, 27, 29, 45, 21]
}

df = pd.DataFrame(data)

# Normalize the data (optional but recommended for K-Means)
normalized_data = (df - df.mean()) / df.std()

# Set the number of clusters
num_clusters = 3

# Initialize centroids randomly
centroids = df.sample(num_clusters)

# Perform K-Means clustering
for _ in range(10):  # Number of iterations
    distances = np.sqrt(((normalized_data.values[:, np.newaxis, :] - centroids.values)**2).sum(axis=2))
    cluster_assignments = np.argmin(distances, axis=1)
    
    for i in range(num_clusters):
        centroids.iloc[i] = normalized_data[cluster_assignments == i].mean()

# Add cluster assignments to the dataframe
df['cluster'] = cluster_assignments

# Print the resulting clusters
for cluster_num in range(num_clusters):
    cluster_data = df[df['cluster'] == cluster_num]
    print(f"Cluster {cluster_num}:\n{cluster_data}\n")
