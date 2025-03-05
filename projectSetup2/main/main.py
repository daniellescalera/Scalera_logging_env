"""
Main module for the calculator application.

This script initializes the calculator, processes user input,
and handles both arithmetic operations and predefined commands.
"""

import os  # Standard library imports
from dotenv import load_dotenv  # Third-party imports

# Project-specific imports
from calculator.calculations import Calculation
from calculator.history import CalculationHistory
from calculator import Calculator
from calculator.logger import logger

# Load environment variables from .env file
load_dotenv()

# Retrieve the ENVIRONMENT variable
environment = os.getenv("ENVIRONMENT")
print(f"Running in {environment} mode")

def main():
    """
    Main function to run the calculator program.

    This function initializes the calculator, prompts the user for input, 
    executes commands or arithmetic operations, and logs all relevant information.
    """
    logger.info("Calculator program started.")  # Log when the program starts

    calculator = Calculator()  # Initialize the Calculator class with command handler
    calculator.start()

    while True:
        print("\nSimple Calculator")
        print("Choose operation: add, subtract, multiply, divide")
        print("Or use commands: greet, goodbye, exit, or menu")
        print("Type 'exit' to quit.")

        user_input = input("Enter operation or command: ").strip().lower()
        logger.info(f"User entered: {user_input}")  # Log user input

        # Check if the input is a command
        if user_input in ["greet", "goodbye", "exit"]:
            logger.info("User entered: %s", user_input)
            calculator.command_handler.execute_command(user_input)
            if user_input == "exit":
                break
            continue

        # Handle arithmetic operations
        if user_input not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Try again.")
            logger.warning("Invalid operation attempted: %s", user_input)
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            calculation = Calculation(user_input, a, b)
            CalculationHistory.add_calculation(calculation)

            result = calculation.result
            print(f"Result: {calculation.result}")
            logger.info("Calculation performed: %s %s %s = %s", a, user_input, b, result)


        except ValueError:
            print("Invalid input. Please enter numeric values.")
            logger.error("User entered a non-numeric value")
        except ZeroDivisionError as e:
            print(e)
            logger.error("Attempted division by zero.")

if __name__ == "__main__":
    main()
