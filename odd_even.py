def check(number):
    if number & 1:
        return f"{number} is odd"
    else:
        return f"{number} is even"
        
num = int(input("\nEnter the number you want to check: "))
print(check(num))