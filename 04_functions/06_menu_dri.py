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

   