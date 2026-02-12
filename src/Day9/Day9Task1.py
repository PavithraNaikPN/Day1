import pandas as pd

# Create the Series with custom labels
products = pd.Series(
    data=[700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard']
)

# Access price of 'Laptop' using label-based indexing
laptop_price = products.loc['Laptop']

# Slice first two products using positional indexing
first_two = products.iloc[0:2]

# Output
print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst Two Products:")
print(first_two)

