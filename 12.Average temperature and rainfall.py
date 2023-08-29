import matplotlib.pyplot as plt

# Sample data: Replace with your actual data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [20, 22, 25, 28, 30, 32, 32, 31, 29, 27, 24, 21]
rainfall = [50, 40, 60, 80, 100, 120, 150, 140, 120, 100, 80, 60]

# 1. Line plot of monthly temperature data
plt.figure(figsize=(10, 6))
plt.plot(months, temperature, marker='o', linestyle='-', color='b')
plt.title('Monthly Temperature Data')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# 2. Scatter plot of monthly rainfall data
plt.figure(figsize=(10, 6))
plt.scatter(months, rainfall, color='r', marker='o')
plt.title('Monthly Rainfall Data')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()






