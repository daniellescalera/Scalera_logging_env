from calculator.commands.command import Command

class ExampleCommand(Command):
    """a sample plugin command that says 'this is an example plugin'"""

    def execute(self) -> None:
        print("this is an example plugin!")