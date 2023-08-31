import numpy as np
import pandas as pd
from scipy import stats

df={"Concentration":[10,20,18,17,15,14]}

# User inputs
sample_size = int(input("Enter the sample size: "))
confidence_level = float(input("Enter the confidence level (between 0 and 1): "))
desired_precision = float(input("Enter the desired level of precision: "))

# Sample data
sample_data = np.array(df["Concentration"])

# Calculate sample mean and standard deviation
sample_mean = np.mean(sample_data)
sample_std = np.std(sample_data)

# Calculate t-score for the given confidence level and degrees of freedom
degrees_freedom = sample_size - 1
t_score = stats.t.ppf(1 - (1 - confidence_level) / 2, degrees_freedom)

# Calculate margin of error
margin_of_error = t_score * (sample_std / np.sqrt(sample_size))

# Calculate confidence interval
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

# Calculate required sample size for desired precision
required_sample_size = ((t_score * sample_std) / desired_precision) ** 2

# Print results
print("\nResults:")
print(f"Sample Mean: {sample_mean:.2f}")
print(f"Sample Standard Deviation: {sample_std:.2f}")
print(f"Confidence Interval: {confidence_interval[0]:.2f} - {confidence_interval[1]:.2f}")
print(f"Required Sample Size for Desired Precision: {int(np.ceil(required_sample_size))}")
