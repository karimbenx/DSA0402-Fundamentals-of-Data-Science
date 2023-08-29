import numpy as np
from scipy.stats import ttest_ind

# Conversion rate data for designs A and B
conversion_rate_design_A = np.array([0.12, 0.15, 0.18, 0.13, 0.16, 0.11, 0.14, 0.17, 0.12, 0.15])
conversion_rate_design_B = np.array([0.09, 0.11, 0.08, 0.10, 0.12, 0.09, 0.11, 0.10, 0.08, 0.10])

# Perform two-sample t-test
t_statistic, p_value = ttest_ind(conversion_rate_design_A, conversion_rate_design_B)

# Significance level
alpha = 0.05

# Compare p-value to significance level
if p_value < alpha:
    print("There is a statistically significant difference between website designs A and B.")
else:
    print("There is no statistically significant difference between website designs A and B.")
