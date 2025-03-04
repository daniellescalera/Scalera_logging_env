"""
module: command_handler.py
"""

class CommandHandler:
    """handles the registration and execution of commands in the application"""

    def __init__(self):
        """initializes the CommandHandler with an empty dictionary of commands"""
        self.commands = {}

    def register_command(self, name: str, command):
        """
        Registers a command with the CommandHandler.
        
        Args:
            name (str): The name of the command.
            command: An object with an execute() method to run the command.
        """
        self.commands[name] = command

    def execute_command(self, name: str):
        """
        Executes a registered command by name.
        Args:
            name (str): The name of the command to execute.    
        Prints:
            Executes the command if found, otherwise notifies the user of an unknown command.
        """
        if name in self.commands:
            self.commands[name].execute()
        else:
            print(f"Unknown command: {name}")

    def get_available_commands(self) -> list[str]:
        """return a list of available command names"""
        return list(self.commands.keys())