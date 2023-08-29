import matplotlib.pyplot as plt

# Sample data: Replace with your actual data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1200, 1400, 1300, 1600, 1500, 1700]

# Create a figure with subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Line plot
ax1.plot(months, sales, marker='o', linestyle='-', color='b')
ax1.set_title('Monthly Sales Trend')
ax1.set_xlabel('Months')
ax1.set_ylabel('Sales')
ax1.grid(True)

# Scatter plot
ax2.scatter(months, sales, color='r', marker='o')
ax2.set_title('Monthly Sales Scatter Plot')
ax2.set_xlabel('Months')
ax2.set_ylabel('Sales')
ax2.grid(True)

# Bar plot
ax3.bar(months, sales, color='g')
ax3.set_title('Monthly Sales Bar Plot')
ax3.set_xlabel('Months')
ax3.set_ylabel('Sales')
ax3.grid(True)

# Adjust layout and display
plt.tight_layout()
plt.show()
