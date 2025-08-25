
import math
from utils import get_numeric_input, display_error, get_menu_choice

class ScientificCalculator:
    def __init__(self, history_manager):
        self.history_manager = history_manager
        self.angle_mode = "degrees"  # Default angle mode: degrees or radians

    def toggle_angle_mode(self):
        """Toggle between degrees and radians"""
        self.angle_mode = "radians" if self.angle_mode == "degrees" else "degrees"
        return self.angle_mode

    def convert_angle(self, angle):
        """Convert angle based on current mode"""
        if self.angle_mode == "degrees":
            return math.radians(angle)  # Convert to radians for math functions
        return angle

    def sine(self, angle):
        """Calculate sine of an angle"""
        angle_rad = self.convert_angle(angle)
        return math.sin(angle_rad)

    def cosine(self, angle):
        """Calculate cosine of an angle"""
        angle_rad = self.convert_angle(angle)
        return math.cos(angle_rad)

    def tangent(self, angle):
        """Calculate tangent of an angle"""
        angle_rad = self.convert_angle(angle)
        return math.tan(angle_rad)

    def arcsine(self, value):
        """Calculate inverse sine (arcsine)"""
        if value < -1 or value > 1:
            raise ValueError("Value must be between -1 and 1 for inverse trigonometric functions")
        
        result_rad = math.asin(value)
        return math.degrees(result_rad) if self.angle_mode == "degrees" else result_rad

    def arccosine(self, value):
        """Calculate inverse cosine (arccosine)"""
        if value < -1 or value > 1:
            raise ValueError("Value must be between -1 and 1 for inverse trigonometric functions")
        
        result_rad = math.acos(value)
        return math.degrees(result_rad) if self.angle_mode == "degrees" else result_rad

    def arctangent(self, value):
        """Calculate inverse tangent (arctangent)"""
        result_rad = math.atan(value)
        return math.degrees(result_rad) if self.angle_mode == "degrees" else result_rad

    def logarithm(self, value, base=10):
        """Calculate logarithm with specified base"""
        if value <= 0:
            raise ValueError("Logarithm is only defined for positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")
        
        return math.log(value, base)

    def natural_log(self, value):
        """Calculate natural logarithm (base e)"""
        if value <= 0:
            raise ValueError("Natural logarithm is only defined for positive numbers")
        return math.log(value)

    def exponential(self, value):
        """Calculate e raised to the power of value"""
        return math.exp(value)

    def power(self, base, exponent):
        """Calculate base raised to the power of exponent"""
        return math.pow(base, exponent)

    def factorial(self, n):
        """Calculate factorial of a number"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if not isinstance(n, int):
            raise ValueError("Factorial is only defined for integers")
        if n > 100:  # Reasonable limit to prevent excessive computation
            raise ValueError("Factorial calculation is limited to numbers ≤ 100")
        
        return math.factorial(n)

    def absolute_value(self, value):
        """Calculate absolute value"""
        return abs(value)

    def evaluate_expression(self, expression):
        """Evaluate a scientific mathematical expression"""
        try:
            # Convert expression to use math functions
            expression = expression.replace("sin", "math.sin")
            expression = expression.replace("cos", "math.cos")
            expression = expression.replace("tan", "math.tan")
            expression = expression.replace("log", "math.log10")
            expression = expression.replace("ln", "math.log")
            expression = expression.replace("sqrt", "math.sqrt")
            expression = expression.replace("pi", "math.pi")
            expression = expression.replace("e", "math.e")

            # Basic safety check
            allowed_chars = set("0123456789+-*/.()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Expression contains invalid characters")

            # Use eval with limited globals for safety
            result = eval(expression, {"__builtins__": None, "math": math})

            # Log to history
            self.history_manager.add_to_history(expression, result)
            return result

        except Exception as e:
            raise ValueError(f"Error evaluating expression: {str(e)}")

    def run(self):
        """Run the scientific calculator interface"""
        while True:
            print("\n" + "="*50)
            print("        SCIENTIFIC CALCULATOR")
            print("="*50)
            print(f"Angle Mode: {self.angle_mode.upper()}")
            print("1.  Trigonometric Functions")
            print("2.  Inverse Trigonometric Functions")
            print("3.  Logarithms")
            print("4.  Exponential Functions")
            print("5.  Power Function")
            print("6.  Factorial")
            print("7.  Absolute Value")
            print("8.  Toggle Angle Mode (Degrees/Radians)")
            print("9.  Evaluate Expression")
            print("10. Back to Main Menu")
            print("="*50)

            try:
                choice = get_menu_choice(10)

                if choice == 1:
                    self.trigonometric_functions()
                elif choice == 2:
                    self.inverse_trigonometric_functions()
                elif choice == 3:
                    self.logarithm_functions()
                elif choice == 4:
                    self.exponential_functions()
                elif choice == 5:
                    self.power_function()
                elif choice == 6:
                    self.factorial_function()
                elif choice == 7:
                    self.absolute_value_function()
                elif choice == 8:
                    self.toggle_angle_mode()
                    print(f"Angle mode changed to: {self.angle_mode.upper()}")
                    input("Press Enter to continue...")
                elif choice == 9:
                    self.evaluate_scientific_expression()
                elif choice == 10:
                    break

            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                break
            except Exception as e:
                display_error(str(e))

    def trigonometric_functions(self):
        """Handle trigonometric function calculations"""
        print("\n--- Trigonometric Functions ---")
        print("1. Sine (sin)")
        print("2. Cosine (cos)")
        print("3. Tangent (tan)")

        try:
            choice = get_menu_choice(3)
            angle = get_numeric_input(f"Enter angle in {self.angle_mode}: ")

            if choice == 1:
                result = self.sine(angle)
                func_name = "sin"
            elif choice == 2:
                result = self.cosine(angle)
                func_name = "cos"
            elif choice == 3:
                result = self.tangent(angle)
                func_name = "tan"

            expression = f"{func_name}({angle})"
            print(f"Result: {expression} = {result}")
            self.history_manager.add_to_history(expression, result)

        except ValueError as e:
            display_error(str(e))

    def inverse_trigonometric_functions(self):
        """Handle inverse trigonometric function calculations"""
        print("\n--- Inverse Trigonometric Functions ---")
        print("1. Arcsine (sin⁻¹)")
        print("2. Arccosine (cos⁻¹)")
        print("3. Arctangent (tan⁻¹)")

        try:
            choice = get_menu_choice(3)
            value = get_numeric_input("Enter value (-1 to 1 for sin⁻¹ and cos⁻¹): ")

            if choice == 1:
                result = self.arcsine(value)
                func_name = "sin⁻¹"
            elif choice == 2:
                result = self.arccosine(value)
                func_name = "cos⁻¹"
            elif choice == 3:
                result = self.arctangent(value)
                func_name = "tan⁻¹"

            unit = "°" if self.angle_mode == "degrees" else " rad"
            expression = f"{func_name}({value})"
            print(f"Result: {expression} = {result}{unit}")
            self.history_manager.add_to_history(f"{expression} = {result}{unit}", result)

        except ValueError as e:
            display_error(str(e))

    def logarithm_functions(self):
        """Handle logarithm calculations"""
        print("\n--- Logarithmic Functions ---")
        print("1. Logarithm (base 10)")
        print("2. Natural Logarithm (base e)")
        print("3. Custom Base Logarithm")

        try:
            choice = get_menu_choice(3)

            if choice == 1:
                value = get_numeric_input("Enter value: ")
                result = self.logarithm(value)
                expression = f"log({value})"
            elif choice == 2:
                value = get_numeric_input("Enter value: ")
                result = self.natural_log(value)
                expression = f"ln({value})"
            elif choice == 3:
                value = get_numeric_input("Enter value: ")
                base = get_numeric_input("Enter base: ")
                result = self.logarithm(value, base)
                expression = f"log{base}({value})"

            print(f"Result: {expression} = {result}")
            self.history_manager.add_to_history(expression, result)

        except ValueError as e:
            display_error(str(e))

    def exponential_functions(self):
        """Handle exponential function calculations"""
        print("\n--- Exponential Functions ---")
        print("1. e^x")
        print("2. 10^x")

        try:
            choice = get_menu_choice(2)
            exponent = get_numeric_input("Enter exponent: ")

            if choice == 1:
                result = self.exponential(exponent)
                expression = f"e^{exponent}"
            elif choice == 2:
                result = math.pow(10, exponent)
                expression = f"10^{exponent}"

            print(f"Result: {expression} = {result}")
            self.history_manager.add_to_history(expression, result)

        except ValueError as e:
            display_error(str(e))

    def power_function(self):
        """Handle power function calculations"""
        try:
            base = get_numeric_input("Enter base: ")
            exponent = get_numeric_input("Enter exponent: ")

            result = self.power(base, exponent)
            expression = f"{base}^{exponent}"

            print(f"Result: {expression} = {result}")
            self.history_manager.add_to_history(expression, result)

        except ValueError as e:
            display_error(str(e))

    def factorial_function(self):
        """Handle factorial calculations"""
        try:
            n = get_numeric_input("Enter a non-negative integer: ")

            if n != int(n):
                raise ValueError("Factorial requires an integer value")

            n = int(n)
            result = self.factorial(n)
            expression = f"{n}!"

            print(f"Result: {expression} = {result}")
            self.history_manager.add_to_history(expression, result)

        except ValueError as e:
            display_error(str(e))

    def absolute_value_function(self):
        """Handle absolute value calculations"""
        try:
            value = get_numeric_input("Enter a number: ")

            result = self.absolute_value(value)
            expression = f"|{value}|"

            print(f"Result: {expression} = {result}")
            self.history_manager.add_to_history(expression, result)

        except ValueError as e:
            display_error(str(e))

    def evaluate_scientific_expression(self):
        """Evaluate a scientific expression"""
        print("\n--- Expression Evaluation ---")
        print("You can use: sin, cos, tan, log, ln, sqrt, pi, e")
        print("Example: sin(45) + log(100) * sqrt(25)")

        try:
            expression = input("Enter expression: ").strip()

            if not expression:
                print("No expression entered.")
                return

            result = self.evaluate_expression(expression)
            print(f"Result: {expression} = {result}")

        except ValueError as e:
            display_error(str(e))


if __name__ == "__main__":
    # For testing without the full app
    from history import HistoryManager
    hm = HistoryManager()
    calc = ScientificCalculator(hm)
    calc.run()
