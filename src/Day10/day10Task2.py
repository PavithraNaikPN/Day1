import pandas as pd

# Load the CSV file
df = pd.read_csv("sample_price_data.csv")

# 1️⃣ Check initial data types
print("Before cleaning:")
print(df.dtypes)

# 2️⃣ Remove '$' symbol and convert Price to float
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

# 3️⃣ Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Check updated data types
print("\nAfter cleaning:")
print(df.dtypes)

# Optional: Calculate average price
print("\nAverage Price:", df["Price"].mean())

