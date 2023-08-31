import pandas as pd
import matplotlib.pyplot as plt

# Load the soccer player data into a pandas dataframe
df = pd.read_csv('soccer_player_data.csv')

# Find the top 5 players with the highest number of goals scored
top_goalscorers = df.nlargest(5, 'goals_scored')
print('Top 5 players with the highest number of goals scored:')
print(top_goalscorers[['name', 'goals_scored']])

# Find the top 5 players with the highest salaries
top_earners = df.nlargest(5, 'weekly_salary')
print('Top 5 players with the highest salaries:')
print(top_earners[['name', 'weekly_salary']])

# Calculate the average age of players
avg_age = df['age'].mean()
print(f'The average age of players is {avg_age:.2f} years.')

# Display the names of players who are above the average age
above_avg_age = df[df['age'] > avg_age]['name']
print('Players above the average age:')
print(above_avg_age)

# Visualize the distribution of players based on their positions using a bar chart
position_counts = df['position'].value_counts()
plt.bar(position_counts.index, position_counts.values)
plt.title('Player Positions')
plt.xlabel('Position')
plt.ylabel('Count')
plt.show()
