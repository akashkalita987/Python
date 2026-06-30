def is_palindrome(number):
    temp = number
    reverse_num = 0
    
    # Reverse the number mathematically
    while temp > 0:
        digit = temp % 10                # Gets the last digit
        reverse_num = (reverse_num * 10) + digit  # Builds the reversed number
        temp //= 10                      # Removes the last digit
        
    # Return True if original matches reversed, otherwise False
    return reverse_num == number


# --- Test with one number ---
num = 121

if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")