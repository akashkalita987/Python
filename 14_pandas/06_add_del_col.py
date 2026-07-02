import pandas as pd

data = {
    'Item': ['Apple', 'Banana'],
    'Price': [1.2, 0.5],
    'Quantity': [10, 20]
}
df = pd.DataFrame(data)

# Add a new column 'Total_Cost'
df['Total_Cost'] = df['Price'] * df['Quantity']
print("After adding Total_Cost:")
print(df)

# Drop the 'Quantity' column
df = df.drop(columns=['Quantity'])
print("\nAfter dropping Quantity:")
print(df)