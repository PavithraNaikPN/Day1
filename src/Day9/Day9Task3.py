import pandas as pd

# Create the Series
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Clean the usernames
cleaned_usernames = usernames.str.strip().str.lower()

# Check which names contain the letter 'a'
contains_a = cleaned_usernames.str.contains('a')

# Output
print("Cleaned Usernames:")
print(cleaned_usernames)

print("\nNames Containing 'a':")
print(contains_a)

