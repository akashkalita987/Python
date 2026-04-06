original_list = ["DBMS", "OS", "AWP", "AT", "Python"]
reversed_list = []

for item in original_list:
    # Insert each item at the beginning of the new list
    reversed_list.insert(0, item)

print(reversed_list)  # Output: [5, 4, 3, 2, 1]