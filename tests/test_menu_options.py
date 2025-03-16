"""Testing the new menu options"""
import os
import sys
import pytest
from app import App
from calculator.calculations import Calculations
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture(autouse=True)
def clear_calc_history():
    """Clears the calculation history and removes the history file if it exists."""
    Calculations.clear_history()
    history_file = Calculations.history_file
    if os.path.exists(history_file):
        os.remove(history_file)

def test_show_menu(capsys):
    """Test that the REPL menu command prints available commands."""
    app = App()
    app.command_handler.execute_command("menu")
    captured = capsys.readouterr().out
    assert "Commands:" in captured
    assert "- history" in captured
    assert "- clear_history" in captured
    assert "- menu" in captured

def test_show_history_no_file(capsys):
    """Test that 'history' command shows 'No history found' when no history exists."""
    app = App()
    app.command_handler.execute_command("history")  # Call history plugin
    
    captured = capsys.readouterr().out
    assert "No history found" in captured

def test_clear_history(capsys):
    """Test that clear_history deletes the history file and clears history."""
    # Simulate a calculation to create a history file
    from calculator.calculation import Calculation
    from calculator.operations import add
    calc = Calculation.create(4, 2, add)
    Calculations.add_calculation(calc)
    
    # Verify file exists
    assert os.path.exists(Calculations.history_file)

    # Clear history using the command handler
    app = App()
    app.command_handler.execute_command("clear")  # Calls the clear history plugin

    captured = capsys.readouterr().out
    assert "Calculation history cleared" in captured
    assert not os.path.exists(Calculations.history_file)
