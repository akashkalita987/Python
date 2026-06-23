# Number of rows for the triangle
rows = 5

# Outer loop handles the number of rows
for i in range(1, rows + 1):
    # Inner loop handles the number of stars in each row
    for j in range(1, i + 1):
        print("*", end=" ")
    # Print a newline character to move to the next row
    print() 