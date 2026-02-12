import pandas as pd

df = pd.read_csv("location_dirty_data.csv")

# Check unique values before cleaning
print(df["Location"].unique())

# Remove extra spaces
df["Location"] = df["Location"].str.strip()

# Standardize text format
df["Location"] = df["Location"].str.title()   # or use .str.lower()

# Verify fix
print(df["Location"].unique())

