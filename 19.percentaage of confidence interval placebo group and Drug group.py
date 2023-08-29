import numpy as np
import scipy.stats as stats

# Sample data for the drug group and placebo group (replace with your data)
drug_group = np.array([3, 5, 2, 4, 6, 7, 5, 4, 3, 5, 6, 4, 5, 6, 3, 4, 5, 4, 6, 3,
                       5, 2, 4, 6, 7, 5, 4, 3, 5, 6, 4, 5, 6, 3, 4, 5, 4, 6, 3,
                       5, 2, 4, 6, 7, 5, 4, 3, 5, 6])

placebo_group = np.array([5, 7, 4, 6, 8, 9, 7, 6, 5, 7, 8, 6, 7, 8, 5, 6, 7, 6, 8, 5,
                          7, 4, 6, 8, 9, 7, 6, 5, 7, 8, 6, 7, 8, 5, 6, 7, 6, 8, 5,
                          7, 4, 6, 8, 9, 7, 6, 5, 7, 8])

# Calculate sample mean and standard deviation
drug_mean = np.mean(drug_group)
placebo_mean = np.mean(placebo_group)

drug_std = np.std(drug_group, ddof=1)
placebo_std = np.std(placebo_group, ddof=1)

# Calculate t-score for 95% confidence interval
confidence_level = 0.95
degrees_freedom = len(drug_group) - 1
t_score = stats.t.ppf((1 + confidence_level) / 2, degrees_freedom)

# Calculate margin of error
drug_margin_of_error = t_score * (drug_std / np.sqrt(len(drug_group)))
placebo_margin_of_error = t_score * (placebo_std / np.sqrt(len(placebo_group)))

# Calculate confidence intervals
drug_confidence_interval = (drug_mean - drug_margin_of_error, drug_mean + drug_margin_of_error)
placebo_confidence_interval = (placebo_mean - placebo_margin_of_error, placebo_mean + placebo_margin_of_error)

print("95% Confidence Interval for Drug Group:", drug_confidence_interval)
print("95% Confidence Interval for Placebo Group:", placebo_confidence_interval)
