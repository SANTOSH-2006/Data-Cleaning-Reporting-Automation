import pandas as pd

# Load dataset
data = pd.read_csv("dirty sales data.csv")

print("Original Data:")
print(data)

# Remove duplicate rows
data = data.drop_duplicates()

# Fill missing Customer_Name with 'Unknown'
data["Customer_Name"] = data["Customer_Name"].fillna("Unknown")

# Fill missing City with 'Not Available'
data["City"] = data["City"].fillna("Not Available")

# Fill missing Sales with average sales
data["Sales"] = data["Sales"].fillna(data["Sales"].mean())

# Save cleaned data
data.to_csv("cleaned sales data.csv", index=False)

print("\nCleaned Data:")
print(data)

print("\nData Cleaning Completed Successfully!")