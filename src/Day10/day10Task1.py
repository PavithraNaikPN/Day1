
import pandas as pd

# 1. Load the dataset
df = pd.read_csv("customer_orders.csv")

# 2. Shape before cleaning
print("Shape before cleaning:", df.shape)

# 3. Missing values report
print("\nMissing values report:")
print(df.isna().sum())

# 4. Fill missing numeric values with median
numeric_cols = df.select_dtypes(include="number")
df[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.median())

# 5. Remove duplicate rows
df = df.drop_duplicates()

# 6. Shape after cleaning
print("\nShape after cleaning:", df.shape)

# 7. (Optional) Preview cleaned data
print("\nCleaned Data Preview:")
print(df)