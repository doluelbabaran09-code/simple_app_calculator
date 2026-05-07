from random import choice


class CalculatorBase:
    def __init__(self, num1, num2):
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
        elif self.operation == "/":
            if self.num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            return self.num1 / self.num2
        else:
            return "Invalid Operation"

def run_calculator():
    print('\n ---- SIMPLE APP CALCULATOR ---- \n')
    print("Options: +, -, *, /,")
    choice = input("Choose an operation: ").strip()
    
    try:
        val1 = float(input("Enter the first number: "))
        val2 = float(input("Enter the second number: "))
        num1 = float(val1)
        num2 = float(val2)
        calc = Operations(num1, num2, choice)
        result = calc.operations()
        print(f"\n RESULT: {result}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except ZeroDivisionError as e:
        print(f"\n Math Error: {e}")
    
    retry = input("\n Do you want to perform another calculation? (y/n): ").lower()
    if retry == "y":
        run_calculator()
    else:
        print("Thank you for using the calculator. Goodbye!")

if __name__ == "__main__":
    run_calculator()
