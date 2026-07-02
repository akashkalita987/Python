import pandas as pd

data = {'Salary': [50000, 60000, 55000, 80000, 120000]}
df = pd.DataFrame(data)

# Get a quick mathematical summary
print("Descriptive Statistics:")
print(df.describe())

# Get a specific metric
print(f"\nAverage Salary: {df['Salary'].mean()}")