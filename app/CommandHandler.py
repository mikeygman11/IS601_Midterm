from calculator import Calculator

class CommandHandler:
    def __init__(self):
        """Initialize the command handler with an empty dictionary for commands."""
        self.commands = {}

    def register_command(self, command_name, function):
        """Registers a command to be callable in the REPL."""
        self.commands[command_name] = function

    def execute_command(self, command_name, *args):
        """Executes the given command if it exists."""
        if command_name not in self.commands:
            raise KeyError(f"Unknown command: {command_name}")
        return self.commands[command_name](*args)