# Get numbers from user
n = int(input("How many numbers do you want to enter? "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate sum of odd and even numbers
sum_odd = 0
sum_even = 0

for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

# Calculate difference
difference = sum_odd - sum_even

print(f"\nSum of odd numbers: {sum_odd}")
print(f"Sum of even numbers: {sum_even}")
print(f"Difference (Odd - Even): {difference}")