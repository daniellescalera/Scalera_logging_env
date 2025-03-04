"""Importing operations, calculation, and calculation history."""
from .operations import Operations
from .calculations import Calculation
from .history import CalculationHistory

from .commands.command_handler import CommandHandler
from .commands.greet_command import GreetCommand
from .commands.goodbye_command import GoodbyeCommand
from .commands.exit_command import ExitCommand
from .commands.plugin_loader import PluginLoader
from .commands.menu import MenuCommand

__all__ = [
    "Operations",
    "Calculation",
    "CalculationHistory",
    "CommandHandler",
    "GreetCommand",
    "GoodbyeCommand",
    "ExitCommand",
    "MenuCommand",
    "PluginLoader",
    ]

class Calculator:
    """main calculator application with dynamic plugin support"""
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self) -> None:
        """registering built-in commands with the command handler"""
        # Registering built-in commands with the command handler
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))

        # Dynamically load plugin commands
        PluginLoader.load_plugins(self.command_handler)

        print("\nSimple Calculator")
        print("Choose operation: add, subtract, multiply, divide")
        print("Or use commands: greet, goodbye, exit, or any loaded plugin commands")
        print("To see the menu, please type 'menu'")
        print("Type 'exit' to quit.")

        while True:
            user_input = input("Enter operation or command: ").strip().lower()

            # Handle registered commands first
            if user_input in self.command_handler.get_available_commands():
                self.command_handler.execute_command(user_input)
                if user_input == "exit":
                    break
                continue

            # Handle arithmetic operations
            if user_input not in ["add", "subtract", "multiply", "divide"]:
                print("Invalid operation. Try again.")
                continue

            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                calculation = Calculation(user_input, a, b)
                CalculationHistory.add_calculation(calculation)

                print(f"Result: {calculation.result}")

            except ValueError:
                print("Invalid input. Please enter numeric values.")
            except ZeroDivisionError as e:
                print(e)
