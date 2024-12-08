class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero is not allowed"

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))

calculator = Calculator(num1, num2)
print("Sum:", calculator.add())
print("Difference:", calculator.sub())
print("Product:", calculator.mul())
print("Division:", calculator.div())