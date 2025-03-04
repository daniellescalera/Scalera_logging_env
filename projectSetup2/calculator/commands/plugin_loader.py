import importlib
import pkgutil
import calculator.plugins
from .command import Command
from .command_handler import CommandHandler

class PluginLoader:
    """Dynamically loads plugin commands from the plugins directory."""

    @staticmethod
    def load_plugins(command_handler: CommandHandler) -> None:
        """Automatically load all commands from the plugins module."""
        # Iterate over all modules in the 'plugins' directory
        for _, module_name, _ in pkgutil.iter_modules(calculator.plugins.__path__):
            module = importlib.import_module(f"calculator.plugins.{module_name}")
            
            # Iterate through attributes in the module to find Command subclasses
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                    # Register the plugin command using its class name as the command keyword
                    command_name = attribute_name.lower().replace("command", "")
                    command_handler.register_command(command_name, attribute())
                    print(f"Loaded plugin command: {command_name}")
