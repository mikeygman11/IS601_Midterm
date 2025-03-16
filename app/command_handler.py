"""
Defines the CommandHandler class, which allows registering and executing
commands dynamically in the REPL environment.
"""
class CommandHandler:
    """registering and running commands: add, subtract, etc"""
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, function):
        """Registers a command to be callable in the REPL."""
        self.commands[command_name] = function

    def execute_command(self, command, *args):
        """executes a command from CommandHandler"""
        if command in self.commands:
            return self.commands[command](*args)
        raise KeyError(f"Unknown command: {command}")
