# Question 4: The Fibonacci numbers are the sequence of integers in which each is the 
# sum of the previous two, with the first two numbers being 1, 1. Thus the first few 
# members of the sequence are 1, 1, 2, 3, 5, 8, 13, 21.
# Calculate Fibonacci numbers up to 100.

# Initializing the first two terms
a, b = 1, 1
print("Fibonacci numbers up to 100:")

while a <= 100:
    print(a, end=" ")
    a, b = b, a + b
print()  # Newline