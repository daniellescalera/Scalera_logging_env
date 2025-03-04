"""This module contains the main functionality for the calculator application."""
from calculator.operations import Operations
from calculator.history import CalculationHistory
from calculator.calculations import Calculation

def main():

    """Interactive calculator program with decimal and whole number support."""
    while True:
        print("\n🔢 Simple Calculator 🔢")
        print("Choose an operation: add, subtract, multiply, divide, history")
        print("Type 'exit' to quit.")

        operation = input("Enter operation: ").strip().lower()

        if operation == "exit":
            print("Goodbye! 👋")
            break  # Exit the loop

        if operation == "history":
            last_calc = CalculationHistory.get_last_calculation()
            if last_calc:
                print(f"📜 Last Calculation: {last_calc}")
            else:
                print("📜 No calculations in history yet.")
            continue

        if operation not in ["add", "subtract", "multiply", "divide"]:
            print("❌ Invalid operation. Please try again.")
            continue

        try:
            num1 = input("Enter first number: ").strip()
            num2 = input("Enter second number: ").strip()

            # Perform the selected operation using Decimal numbers
            if operation == "add":
                result = Operations.add(num1, num2)
            elif operation == "subtract":
                result = Operations.subtract(num1, num2)
            elif operation == "multiply":
                result = Operations.multiply(num1, num2)
            elif operation == "divide":
                result = Operations.divide(num1, num2)

            # Create a calculation instance and add it to history
            calculation = Calculation(operation, float(num1), float(num2))
            CalculationHistory.add_calculation(calculation)
            
            result = calculation.result
            print(f"✅ Result: {result}")

        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.")
        except ZeroDivisionError as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
