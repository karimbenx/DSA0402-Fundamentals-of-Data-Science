import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Simulated data for demonstration
np.random.seed(42)  # For reproducibility
control_group = np.random.normal(loc=50, scale=10, size=100)
treatment_group = np.random.normal(loc=60, scale=10, size=100)

# Calculate basic statistics
control_mean = np.mean(control_group)
treatment_mean = np.mean(treatment_group)
control_std = np.std(control_group)
treatment_std = np.std(treatment_group)

# Perform two-sample t-test
t_stat, p_value = stats.ttest_ind(treatment_group, control_group)

# Print statistics and p-value
print('Control Group Mean:', control_mean)
print('Treatment Group Mean:', treatment_mean)
print('Control Group Standard Deviation:', control_std)
print('Treatment Group Standard Deviation:', treatment_std)
print('T-Statistic:', t_stat)
print('P-Value:', p_value)

# Visualize the data with box plot
plt.boxplot([control_group, treatment_group], labels=['Control', 'Treatment'])
plt.title('Clinical Trial Results')
plt.ylabel('Values')
plt.show()

# Interpretation based on p-value
alpha = 0.05
if p_value < alpha:
    print('The p-value is below the significance level. Reject the null hypothesis.')
    print('There is a statistically significant difference between the treatment and control groups.')
else:
    print('The p-value is not below the significance level. Fail to reject the null hypothesis.')
    print('There is no statistically significant difference between the treatment and control groups.')
