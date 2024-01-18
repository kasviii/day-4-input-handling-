from decimal import Decimal  

item_prices = []
while True:
  price = input("Enter the price of an item (or type 'done' to finish): ")
  if price.lower() == "done":
    break
  item_prices.append(Decimal(price))  
tax_rate = Decimal(input("Enter the tax rate as a decimal (e.g., 0.08 for 8%): "))
total_cost = sum(item_prices) * (Decimal(1) + tax_rate)
print(f"Total Cost: ₹{total_cost:.2f}")
