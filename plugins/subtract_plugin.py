"""Creates and registers the subtract plugin"""

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def register(command_handler):
    """Registers the 'subtract' command with the command handler."""
    command_handler.register_command("subtract", subtract)
