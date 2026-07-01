import numpy as np

print("--- 5. Stacking & Splitting ---")
array_x = np.array([1, 2, 3])
array_y = np.array([4, 5, 6])

# Stack horizontally (side-by-side)
h_stacked = np.hstack((array_x, array_y))
print(f"Horizontally Stacked: {h_stacked}")

# Stack vertically (row-wise)
v_stacked = np.vstack((array_x, array_y))
print(f"Vertically Stacked:\n{v_stacked}")

# Split an array into 3 equal parts
large_array = np.array([10, 20, 30, 40, 50, 60])
splits = np.split(large_array, 3)
print(f"\nSplit into 3 parts: {splits}")