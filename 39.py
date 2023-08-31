import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the transaction data into a pandas dataframe
df = pd.read_csv('transaction_data.csv')

# Preprocess the data by scaling numerical variables
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Choose an appropriate number of clusters using the elbow method
inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)
    inertias.append(kmeans.inertia_)
    
plt.plot(range(1, 11), inertias)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

# Fit the K-Means clustering model to the data and predict cluster labels
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(df_scaled)
labels = kmeans.predict(df_scaled)

# Analyze the resulting clusters to identify distinct groups of customers with similar spending and purchase behavior
df['cluster'] = labels
print(df.groupby('cluster').mean())

# Visualize the clusters using scatter plots or other appropriate visualizations to gain insights into customer distribution and distinguish different segments
plt.scatter(df['total_amount'], df['num_items'], c=df['cluster'])
plt.title('Customer Segmentation')
plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Items Purchased')
plt.show()
