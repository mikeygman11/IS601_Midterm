import sys
import os
import logging
import pytest
from app.command_handler import CommandHandler
from plugins.load_plugins import load_plugins
from plugins.add_plugin import add
from plugins.subtract_plugin import subtract
from plugins.multiply_plugin import multiply
from plugins.divide_plugin import divide

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
@pytest.fixture
def command_handler():
    """Fixture to create a new CommandHandler instance for testing plugins."""
    ch = CommandHandler()
    load_plugins(ch)
    return ch

def test_plugins_load(command_handler):
    """Check if the plugins correctly register commands."""
    expected_commands = {"add", "subtract", "multiply", "divide"}
    registered_commands = set(command_handler.commands.keys())
    assert expected_commands.issubset(registered_commands)

def test_add():
    """testing add function"""
    assert add(5, 3) == 8
    assert add(-2, 4) == 2
    assert add(0, 0) == 0

def test_subtract():
    """testing subtract function"""
    assert subtract(10, 3) == 7
    assert subtract(5, 8) == -3
    assert subtract(0, 0) == 0

def test_multiply():
    """testing mult function"""
    assert multiply(4, 5) == 20
    assert multiply(-3, 6) == -18
    assert multiply(0, 100) == 0

def test_divide():
    """testing divide function"""
    assert divide(10, 2) == 5
    assert divide(-12, 3) == -4
    assert divide(9, 3) == 3

def test_divide_by_zero():
    """testing dividing by zero, throw error"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_plugins_load_fails(monkeypatch, caplog):
    """Test if plugin loading logs an error when failing."""
    caplog.clear()
    caplog.set_level(logging.ERROR)

    def mock_import_module(_):
        raise ImportError("Mocked ImportError")
    monkeypatch.setattr("importlib.import_module", mock_import_module)
    handler = CommandHandler()
    load_plugins(handler)
    for record in caplog.records:
        print(f"LOG [{record.levelname}]: {record.message}")
    assert any("Failed to load plugin" in record.message for record in caplog.records)