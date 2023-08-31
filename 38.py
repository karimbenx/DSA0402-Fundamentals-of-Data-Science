import pandas as pd

# Load the temperature data into a pandas dataframe
df = pd.read_csv('temperature_data.csv')

# Calculate the mean temperature for each city
mean_temps = df.groupby('city')['temperature'].mean()

# Calculate the standard deviation of temperature for each city
std_devs = df.groupby('city')['temperature'].std()

# Determine the city with the highest temperature range
temp_ranges = df.groupby('city')['temperature'].agg(lambda x: x.max() - x.min())
highest_range_city = temp_ranges.idxmax()

# Find the city with the most consistent temperature
most_consistent_city = std_devs.idxmin()

# Print out the results
print('Mean temperatures:')
print(mean_temps)
print()
print('Standard deviations:')
print(std_devs)
print()
print(f'The city with the highest temperature range is {highest_range_city}.')
print(f'The city with the most consistent temperature is {most_consistent_city}.')
