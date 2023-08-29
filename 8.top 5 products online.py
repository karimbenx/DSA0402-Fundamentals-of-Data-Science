import pandas as pd

# Read the CSV file into a DataFrame
sales_data = pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/python/Amazon Sale Report.csv")

# Group data by product_name and sum the quantities sold
product_sales = sales_data.groupby('Category')['Qty'].sum()

# Get the top 5 products with the highest sales
top_products = product_sales.nlargest(5)

# Print the top 5 products
print("Top 5 products by sales:")
print(top_products)
