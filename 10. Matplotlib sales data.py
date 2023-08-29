import matplotlib.pyplot as plt

# Sample data: Replace with your actual data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','July','August','September','October','November','December']
sales = [1200, 1400, 1300, 1600, 1500, 1700, 1800, 1900, 2000, 2100, 2200, 2300]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
# 1. Line plot of monthly sales data

ax1.plot(months, sales, marker='o', linestyle='-', color='b')
ax1.set_title('Monthly Sales Data')
ax1.set_xlabel('Months')
ax1.set_ylabel('Sales')
ax1.grid(True)


# 2. Bar plot of monthly sales data

ax2.bar(months, sales, color='b')
ax2.set_title('Monthly Sales Data(Bar Plot)')
ax2.set_xlabel('Months')
ax2.set_ylabel('Sales')
ax2.grid(True)


plt.tight_layout()
plt.show()
