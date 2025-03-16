"""Creates and registers the subtract plugin"""
from calculator import Calculator

def subtract(a, b):
    """Returns the difference between two numbers."""
    return Calculator.subtract(a, b)

def register(command_handler):
    """Registers the 'subtract' command with the command handler."""
    command_handler.register_command("subtract", subtract)
