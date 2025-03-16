"""Testing the calculator plugins"""
import sys
import os
import pkgutil
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


def test_plugins_load_no_register(monkeypatch, caplog):
    """Test that load_plugins logs a warning if a plugin has no register() function."""
    caplog.clear()
    caplog.set_level(logging.WARNING)
    
    # Create a dummy plugin module without a register function.
    class DummyPlugin:
        pass

    def mock_import_module(name):
        return DummyPlugin

    # Simulate pkgutil.iter_modules yielding a plugin.
    def mock_iter_modules(path):
        yield (None, "dummy_plugin", False)
    
    monkeypatch.setattr("importlib.import_module", mock_import_module)
    monkeypatch.setattr(pkgutil, "iter_modules", mock_iter_modules)
    
    handler = CommandHandler()
    load_plugins(handler)
    
    # Check that a warning was logged about the missing register() function.
    assert any("does not have a register() function" in record.message for record in caplog.records)

def test_plugins_directory_missing(monkeypatch, caplog):
    """Test that load_plugins logs a warning when the plugins directory is missing."""
    caplog.clear()
    caplog.set_level(logging.WARNING)
    monkeypatch.setattr(os.path, "exists", lambda path: False if "plugins" in path else True)
    handler = CommandHandler()
    load_plugins(handler)
    # Check that a warning about the plugins directory is logged.
    assert any("Plugins directory" in record.message for record in caplog.records)
