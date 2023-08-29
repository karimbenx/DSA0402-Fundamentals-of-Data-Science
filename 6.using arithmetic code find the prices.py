# Item prices and quantities
item_prices = [2.5, 3.0, 1.75, 4.5]
item_quantities = [3, 2, 5, 1]

# Discount rate and tax rate (as percentages)
discount_rate = 10  # 10% discount
tax_rate = 8       # 8% tax

# Calculate total cost before discounts and taxes
total_cost_before_discounts = sum(price * quantity for price, quantity in zip(item_prices, item_quantities))

# Calculate total discount
total_discount = (discount_rate / 100) * total_cost_before_discounts

# Calculate discounted cost after applying the discount
discounted_cost = total_cost_before_discounts - total_discount

# Calculate total tax
total_tax = (tax_rate / 100) * discounted_cost

# Calculate final total cost including discounts and taxes
final_total_cost = discounted_cost + total_tax

# Print the results
print(f"Total cost before discounts and taxes: ${total_cost_before_discounts:.2f}")
print(f"Total discount: ${total_discount:.2f}")
print(f"Discounted cost: ${discounted_cost:.2f}")
print(f"Total tax: ${total_tax:.2f}")
print(f"Final total cost: ${final_total_cost:.2f}")
