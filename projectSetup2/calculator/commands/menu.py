from .command import Command
from .command_handler import CommandHandler

class MenuCommand(Command):
    """command to display the avaiable commands"""

    def __init__(self,command_handler: CommandHandler):
        """initialize with a reference to the command handler"""
        self.command_handler = command_handler

    def execute(self) -> None:
        """display the list of available commands"""
        commands = self.command_handler.get_available_commands()
        print("\nAvailable Commands:")
        for command in commands:
            print(f" - {command}")
        print("\nType a command to execute or 'exit' to quit")