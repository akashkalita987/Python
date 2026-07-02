import numpy as np

# 1. Creating Arrays
print("--- 1. Creating Arrays ---")
# Creating a 1D array from a list
arr_1d = np.array([1, 2, 3, 4, 5])
print(f"1D Array: {arr_1d}")

# Creating a 2D array (Matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array:\n{arr_2d}")
print(f"Shape of 2D Array: {arr_2d.shape}\n")

# Generating arrays using built-in helpers
zeros = np.zeros((2, 4))      # 2x4 matrix of zeros
sequence = np.arange(0, 12, 2) # Array from 0 to 8, stepping by 2
print(f"Zeros Matrix:\n{zeros}")
print(f"Sequence Array: {sequence}\n")


# 2. Vectorized Operations (No 'for' loops needed!)
print("--- 2. Vectorized Math ---")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(f"Addition (a + b):        {a + b}")
print(f"Multiplication (a * b):  {a * b}")
print(f"Scalar Math (a * 2):     {a * 2}\n")


# 3. Indexing and Slicing
print("--- 3. Indexing & Slicing ---")
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(f"Specific element (row 1, col 2): {matrix[1, 2]}") 
print(f"First two rows:\n{matrix[:2, :]}")
print(f"Entire second column: {matrix[:, 1]}\n")


# 4. Statistical Methods
print("--- 4. Basic Statistics ---")
data = np.array([1, 5, 3, 9, 2])

print(f"Mean (Average):   {np.mean(data)}")
print(f"Maximum Value:    {np.max(data)}")
print(f"Index of Max Val: {np.argmax(data)}") # Finds the position of the max value