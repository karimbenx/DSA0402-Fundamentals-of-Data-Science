import pandas as pd

# Load the stock data into a pandas dataframe
df = pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/Book10.csv")

# Calculate the daily returns of the stock prices
df['returns'] = df['closing_price'].pct_change()

# Calculate the standard deviation of the daily returns
std_dev = df['returns'].std()

# Print out the results
print(f'The standard deviation of daily returns is {std_dev:.2f}.')
