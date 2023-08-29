import pandas as pd
import matplotlib.pyplot as plt

# Load the user interaction data into a Pandas DataFrame (replace with your actual data)
data = {
    "post_id": [1, 2, 3, 4, 5],
    "likes": [100, 150, 200, 120, 80]
}

df = pd.DataFrame(data)

# Calculate frequency distribution of likes
likes_distribution = df["likes"].value_counts().sort_index()

# Display frequency distribution
print("Likes Frequency Distribution:")
print(likes_distribution)

# Visualize the distribution using a histogram
plt.figure(figsize=(5, 4))
plt.bar(likes_distribution.index, likes_distribution.values)
plt.xlabel("Number of Likes")
plt.ylabel("Frequency")
plt.title("Likes Frequency Distribution among Posts")
plt.show()
