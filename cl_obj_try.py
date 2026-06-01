num =int(input("enter the number"))
even_sum = 0
odd_sum = 0
for numbers in range(1,num+1):
    if numbers%2 == 0:
        print(f"Even numbers are {numbers}")
        even_sum +=numbers
        
    else: 
        print(f"Odd numbers are {numbers}")
        odd_sum += numbers
print(f"Difference between sum of odd and even sum is\n{even_sum-odd_sum}")