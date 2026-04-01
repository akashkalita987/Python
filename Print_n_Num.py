n_str = input("Enter how many numbers you want to input: ")
if n_str.isdigit():
    n = int(n_str)
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        numbers = []
        for i in range(1, n + 1):
            x = input(f"Enter number {i}: ")
            if x.lstrip('-').isdigit():
                numbers.append(int(x))
            else:
                print("Invalid input, storing 0 by default.")
                numbers.append(0)
        print("You entered:")
        for num in numbers:
            print(num)
else:
    print("Invalid input: please enter a positive integer.")
