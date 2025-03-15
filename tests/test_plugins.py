import sys
import os
import pytest
from app.CommandHandler import CommandHandler
from plugins.load_plugins import load_plugins

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