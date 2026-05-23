import pandas as pd

data = pd.read_csv("dirty sales data.csv")

print("Original Data:")
print(data)

data = data.drop_duplicates()
data["Customer_Name"] = data["Customer_Name"].fillna("Unknown")

data["City"] = data["City"].fillna("Not Available")

data["Sales"] = data["Sales"].fillna(data["Sales"].mean())

data.to_csv("cleaned sales data.csv", index=False)

print("\nCleaned Data:")
print(data)

print("\nData Cleaning Completed Successfully!")
