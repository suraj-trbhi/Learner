import math

class Calculator:
    """A comprehensive calculator with basic and advanced operations."""
    
    def add(self, a, b):
        """Addition: a + b"""
        return a + b
    
    def subtract(self, a, b):
        """Subtraction: a - b"""
        return a - b
    
    def multiply(self, a, b):
        """Multiplication: a * b"""
        return a * b
    
    def divide(self, a, b):
        """Division: a / b"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    def power(self, a, b):
        """Power: a ^ b"""
        return a ** b
    
    def square_root(self, a):
        """Square root of a"""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return math.sqrt(a)
    
    def percentage(self, a, b):
        """Calculate a% of b"""
        return (a / 100) * b
    
    def factorial(self, n):
        """Calculate factorial of n"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers!")
        if n == 0 or n == 1:
            return 1
        return math.factorial(n)
    
    def sin(self, x):
        """Sine function (x in radians)"""
        return math.sin(x)
    
    def cos(self, x):
        """Cosine function (x in radians)"""
        return math.cos(x)
    
    def tan(self, x):
        """Tangent function (x in radians)"""
        return math.tan(x)
    
    def log(self, x, base=math.e):
        """Logarithm of x with given base (default: natural log)"""
        if x <= 0:
            raise ValueError("Logarithm not defined for non-positive numbers!")
        if base == math.e:
            return math.log(x)
        return math.log(x, base)

def display_menu():
    """Display calculator menu"""
    print("\n" + "="*50)
    print("           PYTHON CALCULATOR")
    print("="*50)
    print("Available operations:")
    print("1.  Addition (+)")
    print("2.  Subtraction (-)")
    print("3.  Multiplication (*)")
    print("4.  Division (/)")
    print("5.  Power (^)")
    print("6.  Square Root (√)")
    print("7.  Percentage (%)")
    print("8.  Factorial (!)")
    print("9.  Sine (sin)")
    print("10. Cosine (cos)")
    print("11. Tangent (tan)")
    print("12. Logarithm (log)")
    print("13. Exit")
    print("="*50)

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def main():
    """Main calculator program"""
    calc = Calculator()
    
    print("Welcome to Python Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-13): ").strip()
            
            if choice == '13':
                print("Thank you for using the calculator! Goodbye!")
                break
            
            elif choice == '1':  # Addition
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.add(a, b)
                print(f"Result: {a} + {b} = {result}")
            
            elif choice == '2':  # Subtraction
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.subtract(a, b)
                print(f"Result: {a} - {b} = {result}")
            
            elif choice == '3':  # Multiplication
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.multiply(a, b)
                print(f"Result: {a} * {b} = {result}")
            
            elif choice == '4':  # Division
                a = get_number("Enter dividend: ")
                b = get_number("Enter divisor: ")
                result = calc.divide(a, b)
                print(f"Result: {a} / {b} = {result}")
            
            elif choice == '5':  # Power
                a = get_number("Enter base: ")
                b = get_number("Enter exponent: ")
                result = calc.power(a, b)
                print(f"Result: {a} ^ {b} = {result}")
            
            elif choice == '6':  # Square Root
                a = get_number("Enter number: ")
                result = calc.square_root(a)
                print(f"Result: √{a} = {result}")
            
            elif choice == '7':  # Percentage
                a = get_number("Enter percentage: ")
                b = get_number("Enter number: ")
                result = calc.percentage(a, b)
                print(f"Result: {a}% of {b} = {result}")
            
            elif choice == '8':  # Factorial
                n = int(get_number("Enter a non-negative integer: "))
                result = calc.factorial(n)
                print(f"Result: {n}! = {result}")
            
            elif choice == '9':  # Sine
                x = get_number("Enter angle in radians: ")
                result = calc.sin(x)
                print(f"Result: sin({x}) = {result}")
            
            elif choice == '10':  # Cosine
                x = get_number("Enter angle in radians: ")
                result = calc.cos(x)
                print(f"Result: cos({x}) = {result}")
            
            elif choice == '11':  # Tangent
                x = get_number("Enter angle in radians: ")
                result = calc.tan(x)
                print(f"Result: tan({x}) = {result}")
            
            elif choice == '12':  # Logarithm
                x = get_number("Enter number: ")
                base_choice = input("Enter base (press Enter for natural log): ").strip()
                if base_choice:
                    base = float(base_choice)
                    result = calc.log(x, base)
                    print(f"Result: log_{base}({x}) = {result}")
                else:
                    result = calc.log(x)
                    print(f"Result: ln({x}) = {result}")
            
            else:
                print("Invalid choice! Please select a number from 1-13.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
