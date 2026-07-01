def menu_driven_calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        # 1. Check for exit first
        if choice == "5":
            print("Goodbye!")
            break

        # 2. If choice is valid, get numbers and perform the operation
        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == "2":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == "3":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Run the calculator
menu_driven_calculator()