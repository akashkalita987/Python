import pandas as pd

data = {
    'Product': ['Laptop', 'Mouse', 'Monitor'],
    'Price': [1200, 25, 300],
    'Stock': [5, 25, 8]
}
df = pd.DataFrame(data)

# Selecting a single column
print("Product Column:")
print(df['Product'])

# Selecting multiple columns
print("\nProduct and Price Columns:")
print(df[['Product', 'Price']])