"""Creates and registers the divide plugin"""
from calculator import Calculator

def divide(a, b):
    """Returns the quotient of two numbers, handling division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return Calculator.divide(a, b)

def register(command_handler):
    """Registers the 'divide' command with the command handler."""
    command_handler.register_command("divide", divide)
