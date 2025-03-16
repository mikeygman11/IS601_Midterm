import os
import sys
import pytest
import pandas as pd
from app import App
from calculator.calculations import Calculations
from plugins.load_plugins import load_plugins

# Ensure the project root is in sys.path for module imports.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Fixture to clear calculation history before each test.
@pytest.fixture(autouse=True)
def clear_calc_history():
    Calculations.clear_history()
    # Also remove the CSV file if it exists.
    history_file = Calculations.history_file
    if os.path.exists(history_file):
        os.remove(history_file)

# --- Tests for App's REPL commands ---

def test_show_menu(monkeypatch, capsys):
    """Test that the REPL menu command prints available commands."""
    app = App()
    # Call show_menu directly.
    app.show_menu()
    captured = capsys.readouterr().out
    assert "Commands:" in captured
    assert "- history" in captured
    assert "- clear_history" in captured
    assert "- menu" in captured

def test_show_history_no_file(monkeypatch, capsys):
    """Test that 'history' command shows 'No history found' when no file exists."""
    app = App()
    # Ensure the history file is removed.
    if os.path.exists(Calculations.history_file):
        os.remove(Calculations.history_file)
    app.show_history()
    captured = capsys.readouterr().out
    assert "No history found" in captured

def test_clear_history(monkeypatch, capsys):
    """Test that clear_history deletes the history file and clears history."""
    # Simulate a calculation to create a history file.
    from calculator.calculation import Calculation
    from calculator.operations import add
    calc = Calculation.create(4, 2, add)
    Calculations.add_calculation(calc)
    
    # Verify file exists.
    assert os.path.exists(Calculations.history_file)
    # Clear history using the App method.
    app = App()
    app.clear_history()
    captured = capsys.readouterr().out
    assert "Calculation history cleared" in captured
    assert not os.path.exists(Calculations.history_file)

