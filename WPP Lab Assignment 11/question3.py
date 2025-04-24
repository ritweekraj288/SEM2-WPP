# import pandas as pd
# asking_prices = pd.Series([15000, 18000, 20000, 17000, 22000])fair_prices = pd.Series([16000, 17500, 21000, 18000, 22500])
# good_deals = asking_prices[asking_prices < fair_prices].index.tolist()
# print("Indices of good deals:", good_deals)

import pandas as pd

# Take user input for car asking prices
n = int(input("Enter the number of cars: "))

print("\nEnter the asking prices of the cars:")
asking_prices = pd.Series([int(input(f"Car {i+1} asking price: ")) for i in range(n)])

print("\nEnter the fair prices of the cars:")
fair_prices = pd.Series([int(input(f"Car {i+1} fair price: ")) for i in range(n)])

# Find indices where asking price is less than fair price
good_deals = asking_prices[asking_prices < fair_prices].index.tolist()

# Display results
print("\nGood deals found at indices:", good_deals)