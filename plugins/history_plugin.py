"""Plugin for displaying calculation history."""
from calculator.calculations import Calculations

def history():
    """Displays the stored calculation history."""
    history = Calculations.get_history()
    if history:
        print("\n--- Calculation History ---")
        for calc in history:
            print(calc)
    else:
        print("\nNo history found.")

def register(command_handler):
    """Register the history command."""
    command_handler.register_command("history", history)
