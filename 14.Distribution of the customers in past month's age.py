import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data into a Pandas DataFrame (replace with your actual data)
data = {
    "customer_id": [1, 2, 3, 4, 5, 6],
    "age": [25, 30, 22, 35, 28, 28],
    "purchase_amount": [100, 150, 200, 120, 80, 90]
}

df = pd.DataFrame(data)

# Filter purchases
purchased_df = df[df["purchase_amount"] > 0]

# Calculate frequency distribution of customer ages
age_distribution = purchased_df["age"].value_counts().sort_index()

# Display frequency distribution
print("Age Frequency Distribution:")
print(age_distribution)

# Visualize the distribution using a histogram
plt.figure(figsize=(10, 6))
plt.bar(age_distribution.index, age_distribution.values)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Frequency Distribution of Customers")
plt.show()
