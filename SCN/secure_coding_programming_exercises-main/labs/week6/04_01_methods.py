"""
Create a class (you pick the name) that has
at least 5 methods.
3 of the methods must call other methods within them (using self.method name)
Run at least one method automatically in __init__ so it will run at start up

Demonstrate your methods work by creating an instance and running all the methods
"""
class Calculator:
    def __init__(self):
        self.total = 0
        self.add(5)  # Run a method automatically in __init__

    def add(self, num):
        self.total += num

    def subtract(self, num):
        self.total -= num

    def multiply(self, num):
        self.total *= num

    def divide(self, num):
        if num != 0:
            self.total /= num
        else:
            print("Error: Division by zero is not allowed.")

    def calculate(self, operation, num):
        if operation == 'add':
            self.add(num)
        elif operation == 'subtract':
            self.subtract(num)
        elif operation == 'multiply':
            self.multiply(num)
        elif operation == 'divide':
            self.divide(num)
        else:
            print("Error: Invalid operation.")

# Create an instance of Calculator
calc = Calculator()

# Run all the methods
calc.add(10)
calc.subtract(5)
calc.multiply(3)
calc.divide(2)
calc.calculate('add', 5)

print(f"The total is {calc.total}.")
