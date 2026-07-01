import numpy as np

print("--- 7. Linear Algebra Operations ---")
# Define a square 2x2 matrix
matrix_A = np.array([
    [4, 7],
    [2, 6]
])
print(f"Matrix A:\n{matrix_A}")

# 1. Calculate the Determinant of the matrix
det = np.linalg.det(matrix_A)
print(f"\nDeterminant of Matrix A: {det:.2f}")

# 2. Calculate the Multiplicative Inverse of the matrix
# (An inverse matrix A^-1 satisfies the property: A @ A^-1 = Identity Matrix)
inverse_A = np.linalg.inv(matrix_A)
print(f"\nInverse of Matrix A:\n{inverse_A}")

# Verification: Multiplying a matrix by its inverse results in the Identity Matrix
identity_test = np.dot(matrix_A, inverse_A)
print(f"\nVerification (A @ Inverse) -> Identity Matrix:\n{np.round(identity_test)}")