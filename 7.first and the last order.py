import pandas as pd

# Creating the order_data dictionary
order_data = {
    'customer_id': [1, 2, 3, 4],
    'order_date': ['23/06/2023', '24/05/2023', '26/08/2023', '25/07/2023'],
    'product_name': ['soap', 'towel', 'brush', 'toothpaste'],
    'order_quantity': [1, 2, 3, 4]
}

# Create a DataFrame from the order_data dictionary
order = pd.DataFrame(order_data)

# Print the DataFrame
print(order)

# 1. Total number of orders made by each customer
total_orders_per_customer = order['customer_id'].value_counts()

# 2. Average order quantity for each product
average_quantity_per_product = order.groupby('product_name')['order_quantity'].mean()

# 3. Earliest and latest order dates in the dataset
order['order_date'] = pd.to_datetime(order['order_date'])  # Convert order_date to datetime
earliest_order_date = order['order_date'].min()
latest_order_date = order['order_date'].max()

# Print the results
print("\nTotal number of orders per customer:\n", total_orders_per_customer)
print("\nAverage order quantity per product:\n", average_quantity_per_product)
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
