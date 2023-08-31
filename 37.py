import pandas as pd
import matplotlib.pyplot as plt

# Load the student data into a pandas dataframe
df = pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/Book11.csv")

# Calculate the correlation coefficient between study time and exam scores
corr = df['study_time'].corr(df['exam_score'])

# Print out the correlation coefficient
print(f'The correlation coefficient between study time and exam scores is {corr:.2f}.')

# Visualize the relationship between study time and exam scores using a scatter plot
plt.scatter(df['study_time'], df['exam_score'])
plt.title('Study Time vs. Exam Scores')
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.show()
