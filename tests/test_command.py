import pytest
from app.command_handler import CommandHandler

def test_command_handler_register_and_execute():
    """Test registering and executing a command."""
    def mock_command():
        return "Command executed"

    handler = CommandHandler()
    handler.register_command("test", mock_command)

    assert handler.execute_command("test") == "Command executed"

def test_command_handler_unknown_command():
    """Test handling of unknown commands."""
    handler = CommandHandler()

    with pytest.raises(KeyError):
        handler.execute_command("invalid_command")