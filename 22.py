import pandas as pd
import math
import scipy.stats as stats

# Load the CSV file into a pandas dataframe
df = pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/Customer_reviews.csv")

# Calculate the mean, count, and standard deviation of the ratings for each product
stats = df.groupby('product_id')['rating'].agg(['mean', 'count', 'std'])

# Calculate the 95% confidence interval for each product's mean rating
ci95_hi = []
ci95_lo = []
for i in stats.index:
    m, c, s = stats.loc[i]
    ci95_hi.append(m + 1.96 * s / math.sqrt(c))
    ci95_lo.append(m - 1.96 * s / math.sqrt(c))
stats['ci95_hi'] = ci95_hi
stats['ci95_lo'] = ci95_lo

# Print the resulting dataframe with mean rating, count, standard deviation, and 95% confidence interval
print(stats)
