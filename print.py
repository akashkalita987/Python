fruits = ["apple", "banana", "cherry"]
reversed_list = []

# You must use range() to generate the numbers (2, 1, 0)
for i in range(len(fruits) - 1, -1, -1):
    reversed_list.append(fruits[i])

print(f"Last index used: {i}") # This will print 0
print(f"Reversed list: {reversed_list}")