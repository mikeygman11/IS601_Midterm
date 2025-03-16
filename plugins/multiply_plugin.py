"""Creates and registers the multiplication plugin"""

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def register(command_handler):
    """Registers the 'multiply' command with the command handler."""
    command_handler.register_command("multiply", multiply)
