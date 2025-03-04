from calculator.commands.command_handler import CommandHandler
from calculator.commands.menu import MenuCommand
from calculator.commands.greet_command import GreetCommand

def test_menu_command(capsys):
    """Test that the menu command displays the available commands."""
    command_handler = CommandHandler()

    # Register commands correctly with the proper variable name
    command_handler.register_command("greet", GreetCommand())
    command_handler.register_command("menu", MenuCommand(command_handler))

    # Access and execute the 'menu' command correctly
    menu_command = command_handler.commands["menu"]
    menu_command.execute()

    # Capture and verify the output
    captured = capsys.readouterr()
    assert "Available Commands:" in captured.out
    assert " - greet" in captured.out
    assert " - menu" in captured.out
