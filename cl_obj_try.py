even_sum = 0
odd_sum = 0

# We keep it as a string so we can loop through each digit
num_str = input("Enter the number: ") 

for digit_char in num_str:
    digit = int(digit_char) # Convert the single character back to an integer
    if digit % 2 == 0:
        even_sum += digit
    else: 
        odd_sum += digit

print("\n--- Digit Analysis Results ---")
print(f"Sum of Even Digits (4 + 6): {even_sum}")
print(f"Sum of Odd Digits (3 + 5): {odd_sum}")
print(f"Difference between digit sums: {abs(even_sum - odd_sum)}")