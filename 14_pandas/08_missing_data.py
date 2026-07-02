import pandas as pd
import numpy as np

data = {
    'Name': ['Alex', 'Blake', 'Charlie'],
    'Age': [24, np.nan, 30] # np.nan represents a missing value
}
df = pd.DataFrame(data)

print("Original Data with missing value:")
print(df)

# Fill the missing Age with the average age (27)
df['Age'] = df['Age'].fillna(27)

print("\nAfter filling missing values:")
print(df)