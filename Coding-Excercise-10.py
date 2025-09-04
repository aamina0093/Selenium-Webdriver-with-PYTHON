"""
Understanding class creation in Python
Objective: Create a basic calculator class to perform addition, subtraction, multiplication, and division.

Instructions:

Create a class named BasicCalculator.

Define a constructor that initializes two numbers. Use numbers 10 & 5

Implement methods for:

Addition

Subtraction

Multiplication

Division

Each method should return the result of the operation.

Create an instance of the BasicCalculator class and demonstrate the functionality of each method.

Example Output:

Addition: 10 + 5 = 15
Subtraction: 10 - 5 = 5
Multiplication: 10 * 5 = 50
Division: 10 / 5 = 2.0
"""

class BasicCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.a

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


calc = BasicCalculator(10, 5)

print('Addition', calc.addition())
print('Subtraction', calc.subtraction())
print('Multiplication', calc.multiplication())
print('Division', calc.division())



