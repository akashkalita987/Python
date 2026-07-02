import pandas as pd

# Load a CSV file (replace with your file path)
# df = pd.read_csv('data.csv')

# For demonstration, we'll use our previous DataFrame
data = {'Score': [85, 92, 78, 89, 95, 64, 72]}
df = pd.DataFrame(data)

# View the first 3 rows
print("First 3 rows:")
print(df.head(3))