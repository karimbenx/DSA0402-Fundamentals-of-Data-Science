import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats

# Assuming you have a DataFrame named 'data'
df = pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/python/ageandfat.csv")

# Calculate mean, median, and standard deviation
age_mean = df["age"].mean()
age_median = df["age"].median()
age_std = df["age"].std()

fat_mean = df["%fat"].mean()
fat_median = df["%fat"].median()
fat_std = df["%fat"].std()

print("Age:")
print(f"Mean: {age_mean:.2f}")
print(f"Median: {age_median}")
print(f"Standard Deviation: {age_std:.2f}\n")

print("%Fat:")
print(f"Mean: {fat_mean:.2f}")
print(f"Median: {fat_median}")
print(f"Standard Deviation: {fat_std:.2f}")

# Draw boxplots for age and %fat
plt.figure(figsize=(10, 6))
df.boxplot(column=["age", "%fat"])
plt.title("Boxplots for Age and %Fat")
plt.ylabel("Value")
plt.show()

# Draw scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df["age"], df["%fat"])
plt.title("Scatter Plot of Age vs %Fat")
plt.xlabel("Age")
plt.ylabel("%Fat")
plt.show()

# Draw Q-Q plot for age
plt.figure(figsize=(8, 6))
sm.qqplot(df["age"], line='s')
plt.title("Q-Q Plot for Age")
plt.show()

# Draw Q-Q plot for %fat
plt.figure(figsize=(8, 6))
sm.qqplot(df["%fat"], line='s')
plt.title("Q-Q Plot for %Fat")
plt.show()
