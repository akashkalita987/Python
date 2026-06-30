def is_arm(number):
    temp = number
    count = 0
    while temp > 0:
        count += 1
        temp //= 10
        
    temp = number
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** count
        temp //= 10
    # Move this line OUTSIDE the while loop (un-indent it)
    return total == number 

num = 153

if is_arm(num):
    print(num, "is a armstrong")
else:
    print(num, "is not a armstrong")