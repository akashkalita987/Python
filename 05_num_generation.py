import numpy as np

print("--- 4. Random Sampling & Distributions ---")
# Set a random seed so the results are reproducible
np.random.seed(42)

# Generate 5 random floats between 0 and 1
random_floats = np.random.rand(5)
print(f"Random Floats:\n{random_floats}")

# Generate a 2x3 matrix of random integers between 1 and 100
random_ints = np.random.randint(1, 101, size=(2, 3))
print(f"\nRandom 2x3 Integers Matrix:\n{random_ints}")

# Shuffle an array in-place
items = np.array(["Apple", "Banana", "Cherry", "Date"])
np.random.shuffle(items)
print(f"\nShuffled Items: {items}")