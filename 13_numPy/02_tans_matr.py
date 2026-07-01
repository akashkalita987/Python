import numpy as np

print("--- 1. Reshaping & Transposing ---")
# Create a 1D array of 12 elements
flat_array = np.arange(1, 13)
print(f"Original 1D array:\n{flat_array}")

# Reshape into a 2D matrix (3 rows, 4 columns)
matrix = flat_array.reshape(3, 4)
print(f"\nReshaped to 3x4 Matrix:\n{matrix}")

# Transpose the matrix (swap rows and columns)
transposed = matrix.T
print(f"\nTransposed Matrix (4x3):\n{transposed}")