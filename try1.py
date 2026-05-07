# Keep it as a string so we can iterate through the digits
num = input("Enter the number: ")

odd_sum = 0
even_sum = 0

for digit in num:
    # Convert each digit back to an integer to do math
    n = int(digit)
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

print(f"\nThe difference (Odd Sum - Even Sum) is: {odd_sum - even_sum}")