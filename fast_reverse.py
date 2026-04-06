original = ["Apple", "Banana", "Cherry"]
reversed_list = []

# Start at the last index, end at 0, move by -1 each step
for i in range(len(original) - 1, -1, -1):
    reversed_list.append(original[i])

print(reversed_list)
# Result: ['Cherry', 'Banana', 'Apple']