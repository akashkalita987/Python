import numpy as np

print("--- 3. Matrix Multiplication ---")
# 2x3 matrix
matrix_A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 3x2 matrix
matrix_B = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

# Multiply matrix_A (2x3) by matrix_B (3x2) -> Results in a 2x2 matrix
result = np.dot(matrix_A, matrix_B)
# Alternatively, you can use: result = matrix_A @ matrix_B

print(f"Matrix A:\n{matrix_A}")
print(f"Matrix B:\n{matrix_B}")
print(f"Dot Product Result:\n{result}")