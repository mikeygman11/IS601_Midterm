"""Plugin for clearing calculation history."""
from calculator.calculations import Calculations

def clear_history():
    """Clears stored calculation history."""
    Calculations.clear_history()
    print("\nCalculation history cleared.")

def register(command_handler):
    """Register the clear history command."""
    command_handler.register_command("clear", clear_history)
