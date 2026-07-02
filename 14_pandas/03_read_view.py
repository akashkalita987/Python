import pandas as pd
from pathlib import Path

# Load a CSV file (replace with your file path)
# df = pd.read_csv('data.csv')

# For demonstration, we'll use our previous DataFrame
data = {'Score': [85, 92, 78, 89, 95, 64, 72]}
df = pd.DataFrame(data)

# View the first 3 rows
print("First 3 rows:")
print(df.head(3))

# --- Example: read a CSV placed beside this script ---
# build a path to the CSV located in the same folder as this script
csv_path = Path(__file__).with_name('sample_data.csv')

try:
    df_csv = pd.read_csv(csv_path)
    print('\nSample CSV loaded from:', csv_path)
    print(df_csv.head())
except Exception as e:
    print('\nCould not read CSV at', csv_path)
    print('Error:', e)
