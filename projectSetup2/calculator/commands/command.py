class Command:
    """abstract base class for all commands"""

    def execute(self) -> None:
        """execute the command. must be implemented by subclasses"""
        raise NotImplementedError("subclasses must implement this method.")