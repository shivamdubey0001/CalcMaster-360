import math
from utils import get_numeric_input, display_error

class BasicCalculator:
    def __init__(self, history_manager):
        """Initialize the calculator with history manager and memory"""
        self.history_manager = history_manager
        self.memory = 0  # Memory starts at 0

    # ------------------------------
    # Basic Operations
    # ------------------------------
    def add(self, a, b):
        """Add two numbers"""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a"""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b

    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def square(self, x):
        """Square of a number"""
        return x * x

    def square_root(self, x):
        """Square root of a number"""
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(x)

    def percentage(self, value, percent):
        """Calculate percentage"""
        return (value * percent) / 100

    # ------------------------------
    # Memory Operations
    # ------------------------------
    def memory_add(self, value):
        """Add value to memory"""
        self.memory += value
        return self.memory

    def memory_subtract(self, value):
        """Subtract value from memory"""
        self.memory -= value
        return self.memory

    def memory_recall(self):
        """Recall memory value"""
        return self.memory

    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        return self.memory

    # ------------------------------
    # Expression Evaluation
    # ------------------------------
    def evaluate_expression(self, expression):
        """Evaluate a safe mathematical expression"""
        try:
            allowed_chars = set("0123456789+-*/.() ")
            if not all(c in allowed_chars or c.isalpha() for c in expression):
                raise ValueError("Expression contains invalid characters")

            # Safe eval with only math functions
            result = eval(expression, {"__builtins__": None}, {
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "pi": math.pi,
                "e": math.e
            })

            self.history_manager.add_to_history(expression, result)
            return result

        except Exception as e:
            raise ValueError(f"Error evaluating expression: {str(e)}")

    # ------------------------------
    # User Interface (CLI)
    # ------------------------------
    def run(self):
        """Run calculator menu"""
        while True:
            print("\n" + "="*40)
            print("        BASIC CALCULATOR")
            print("="*40)
            print("1. Simple Calculation")
            print("2. Square")
            print("3. Square Root")
            print("4. Percentage")
            print("5. Memory Functions")
            print("6. Back to Main Menu")
            print("="*40)

            try:
                choice = input("Select an option (1-6): ").strip()

                if choice == "1":
                    self.simple_calculation()
                elif choice == "2":
                    self.calculate_square()
                elif choice == "3":
                    self.calculate_square_root()
                elif choice == "4":
                    self.calculate_percentage()
                elif choice == "5":
                    self.memory_functions()
                elif choice == "6":
                    break
                else:
                    print("Invalid choice. Please try again.")

            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                break
            except Exception as e:
                display_error(str(e))

    # ------------------------------
    # Operations with User Input
    # ------------------------------
    def simple_calculation(self):
        """Two-number calculation"""
        print("\n--- Simple Calculation ---")
        print("Available operators: +, -, *, /")

        try:
            num1 = get_numeric_input("Enter first number: ")
            operator = input("Enter operator (+, -, *, /): ").strip()

            if operator not in ['+', '-', '*', '/']:
                raise ValueError("Invalid operator. Please use +, -, *, or /")

            num2 = get_numeric_input("Enter second number: ")

            if operator == '+':
                result = self.add(num1, num2)
            elif operator == '-':
                result = self.subtract(num1, num2)
            elif operator == '*':
                result = self.multiply(num1, num2)
            elif operator == '/':
                result = self.divide(num1, num2)

            expression = f"{num1} {operator} {num2}"
            print(f"Result: {expression} = {result}")
            self.history_manager.add_to_history(expression, result)

        except ValueError as e:
            display_error(str(e))
        except ZeroDivisionError:
            display_error("Cannot divide by zero")

    def calculate_square(self):
        """Square of number"""
        try:
            num = get_numeric_input("Enter a number to square: ")
            result = self.square(num)
            expression = f"{num}²"
            print(f"Result: {expression} = {result}")
            self.history_manager.add_to_history(expression, result)
        except ValueError as e:
            display_error(str(e))

    def calculate_square_root(self):
        """Square root of number"""
        try:
            num = get_numeric_input("Enter a number to find square root: ")
            result = self.square_root(num)
            expression = f"√{num}"
            print(f"Result: {expression} = {result}")
            self.history_manager.add_to_history(expression, result)
        except ValueError as e:
            display_error(str(e))

    def calculate_percentage(self):
        """Percentage calculation"""
        try:
            value = get_numeric_input("Enter the value: ")
            percent = get_numeric_input("Enter the percentage: ")
            result = self.percentage(value, percent)
            expression = f"{percent}% of {value}"
            print(f"Result: {expression} = {result}")
            self.history_manager.add_to_history(expression, result)
        except ValueError as e:
            display_error(str(e))

    def memory_functions(self):
        """Menu for memory operations"""
        while True:
            print("\n--- Memory Functions ---")
            print(f"Current Memory: {self.memory}")
            print("1. Memory Add (M+)")
            print("2. Memory Subtract (M-)")
            print("3. Memory Recall (MR)")
            print("4. Memory Clear (MC)")
            print("5. Back to Basic Calculator")

            try:
                choice = input("Select an option (1-5): ").strip()

                if choice == "1":
                    value = get_numeric_input("Enter value to add to memory: ")
                    self.memory_add(value)
                    print(f"Added {value} to memory. New value: {self.memory}")
                elif choice == "2":
                    value = get_numeric_input("Enter value to subtract from memory: ")
                    self.memory_subtract(value)
                    print(f"Subtracted {value} from memory. New value: {self.memory}")
                elif choice == "3":
                    value = self.memory_recall()
                    print(f"Memory value: {value}")
                elif choice == "4":
                    self.memory_clear()
                    print("Memory cleared.")
                elif choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")

            except ValueError as e:
                display_error(str(e))
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                break


# ------------------------------
# Example usage
# ------------------------------
if __name__ == "__main__":
    from history import HistoryManager
    hm = HistoryManager()
    calc = BasicCalculator(hm)
    calc.run()
