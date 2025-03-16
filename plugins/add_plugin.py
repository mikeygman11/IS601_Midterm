"""Creates and registers the add plugin"""

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def register(command_handler):
    """Registers the 'add' command with the command handler."""
    command_handler.register_command("add", add)
