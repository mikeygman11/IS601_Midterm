"""Creates and registers the add plugin"""
from calculator import Calculator

def add(a, b):
    """Returns the sum of two numbers."""
    return Calculator.add(a, b)

def register(command_handler):
    """Registers the 'add' command with the command handler."""
    command_handler.register_command("add", add)
