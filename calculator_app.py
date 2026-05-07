class CalculatorBase:
    def __init__(self, num1, num1):
        self.num1 = num1
        self.num2 = num2

class Operations(CalculatorBase):
    def __init__ (self, num1, num2, operation):
        super(). __init__(num1, num2)
        self.operation = operation.strip()

    def operations(self):
        if self.operation == "+":
            return self.num1 + self.num2
        elif self.operation == "-":
            return self.num1 - self.num2
        elif self.operation == "*":
            return self.num1 * self.num2
        elif self.operation == "/"
            return self.num1 / self.num2
        if self.num2 == 0:
            raise ValueDivisionError("Cannot divide by zero!")
        return self.num1 / self.num2
    else: return "Invalid operation!"
