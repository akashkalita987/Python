import numpy as np

print("--- 2. Boolean Masking & Filtering ---")
grades = np.array([85, 42, 90, 65, 55, 100, 72])
print(f"All Grades: {grades}")

# Create a boolean condition (mask)
passing_mask = grades >= 60
print(f"Boolean Mask (>= 60): {passing_mask}")

# Filter the array using the mask
passing_grades = grades[passing_mask]
print(f"Filtered Passing Grades: {passing_grades}")

# Modify elements that match a condition instantly
grades[grades < 60] = 60
print(f"Grades with 'curves' (min 60): {grades}")