def menu_driven_calculator():
    def get_number(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid number. Please enter a valid numeric value.")

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return None
        return a / b

    while True:
        print("\nSimple Menu-Driven Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Enter 1, 2, 3, 4, or 5.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == "1":
            result = add(num1, num2)
            op = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            op = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            op = "*"
        else:
            result = divide(num1, num2)
            op = "/"

        if result is None:
            print("Error: Cannot divide by zero.")
        else:
            print(f"{num1} {op} {num2} = {result}")


if __name__ == "__main__":
    menu_driven_calculator()
