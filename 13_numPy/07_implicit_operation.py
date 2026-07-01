import numpy as np

print("--- 6. Broadcasting Examples ---")
# A 3x3 matrix representing features of 3 different items
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# A 1D array representing a modifier for each column
column_modifier = np.array([1, 2, 3])

# Broadcasting adds the 1D array to every single row of the 2D matrix automatically
broadcast_sum = matrix + column_modifier

print(f"Original Matrix:\n{matrix}")
print(f"\n1D Modifier Array: {column_modifier}")
print(f"\nResult after Broadcasting (Modifier added to each row):\n{broadcast_sum}")