from dotenv import load_dotenv
import os

#load enviornment variables from .env file
load_dotenv()

#retrieve the ENVIRONMENT variable
environment = os.getenv("ENVIRONMENT")

print(f"Running in {environment} mode")
"""importing all of the needed commands"""
from calculator.calculations import Calculation
from calculator.history import CalculationHistory
from calculator import Calculator
from calculator.logger import logger
def main():
    logger.info("Calculator program started.") # log when the program starts

    calculator = Calculator()  # Initialize the Calculator class with command handler
    calculator.start()

    while True:
        print("\nSimple Calculator")
        print("Choose operation: add, subtract, multiply, divide")
        print("Or use commands: greet, goodbye, exit, or menu")
        print("Type 'exit' to quit.")

        user_input = input("Enter operation or command: ").strip().lower()
        logger.info(f"User entered: {user_input} ") #log user input

        # Check if the input is a command
        if user_input in ["greet", "goodbye", "exit"]:
            logger.info(f"Executing command: {user_input} ")
            calculator.command_handler.execute_command(user_input)
            if user_input == "exit":
                break
            continue

        # Handle arithmetic operations
        if user_input not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Try again.")
            logger.warning(f"Invalid operation attempted: {user_input} ")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            calculation = Calculation(user_input, a, b)
            CalculationHistory.add_calculation(calculation)

            result = calculation.result
            print(f"Result: {calculation.result}")
            logger.info(f"Calculation performed: {a} {user_input} {b} = {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
            logger.error("User entered a non-numeric value")
        except ZeroDivisionError as e:
            print(e)
            logger.error("Attempted divison by zero.")

if __name__ == "__main__":
    main()
