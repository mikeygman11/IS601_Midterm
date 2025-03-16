"""Creates and registers the multiplication plugin"""
from calculator import Calculator

def multiply(a, b):
    """Returns the product of two numbers."""
    return Calculator.multiply(a, b)

def register(command_handler):
    """Registers the 'multiply' command with the command handler."""
    command_handler.register_command("multiply", multiply)
