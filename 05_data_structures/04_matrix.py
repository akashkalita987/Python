rows = int(input("Enter the number of rows: "))
colm = int(input("Enter thenumber of columns: "))

matrix = []

print(f"\nenter the elements for a {rows}X{colm} matrix:")

for i in range(rows):
    row= []
    for j in range(colm):
        element = input(f"Element at[{i}][{j}]:")
        row.append(element)
    matrix.append(row)

print("\nYour matrix:")
for row in matrix:
    for item in row:
        print(item,end="\t")
    print()