# 1. Defining the Class (The Blueprint)
class Car:
    # The Constructor method to initialize attributes
    def __init__(self, brand, model, year):
        self.brand = brand    # Instance attribute
        self.model = model    # Instance attribute
        self.year = year      # Instance attribute

    # A method (behavior) of the class
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

    # Another method demonstrating behavior
    def start_engine(self):
        return f"The engine of the {self.model} is now roaring!"


# 2. Creating Objects (Instances of the Class)
car1 = Car("Toyota", "Camry", 2024)
car2 = Car("Tesla", "Model 3", 2025)


# 3. Accessing Attributes and Methods
# Accessing car1
print("--- Car 1 Details ---")
print(f"Brand: {car1.brand}")          # Accessing attribute
print(car1.display_info())             # Calling method
print(car1.start_engine())             # Calling method

print("\n--- Car 2 Details ---")
# Accessing car2
print(f"Brand: {car2.brand}")          # Accessing attribute
print(car2.display_info())             # Calling method
print(car2.start_engine())             # Calling method