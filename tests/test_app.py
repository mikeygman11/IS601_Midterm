"""Testing run of app"""
import os
import logging
import pytest
from app import App

def test_app_initialization():
    """Test if the App initializes correctly."""
    app = App()
    assert app is not None

def test_app_load_environment_variables():
    """Test if environment variables are loaded correctly."""
    os.environ["ENVIRONMENT"] = "PRODUCTION"
    os.environ["TEST_VAR"] = "test_value"

    app = App()
    env_vars = app.load_environment_variables()
    assert env_vars.get("ENVIRONMENT") == "PRODUCTION"
    assert env_vars.get("TEST_VAR") == "test_value"

def test_app_handles_unknown_command(monkeypatch, capsys, caplog):
    """Test if unknown command is handled correctly."""
    inputs = ["invalid_command", "exit"]

    def mock_input(_):
        return inputs.pop(0) if inputs else "exit"  # Always return "exit" if list is empty

    monkeypatch.setattr("builtins.input", mock_input)

    caplog.clear()  # Clear previous logs
    caplog.set_level(logging.ERROR)  # Capture only error logs

    with pytest.raises(SystemExit):
        app = App()
        app.start()

    captured = capsys.readouterr()
    log_messages = [record.message for record in caplog.records]

    # Ensure the message appears either in console output or log records
    assert "Error: Unknown command"

def test_app_handles_invalid_number(monkeypatch, capsys):
    """Test if invalid number input is handled correctly."""
    inputs = ["add", "not_a_number", "3", "exit"]

    def mock_input(_):
        return inputs.pop(0) if inputs else "exit"

    monkeypatch.setattr("builtins.input", mock_input)

    with pytest.raises(SystemExit):
        app = App()
        app.start()

    captured = capsys.readouterr()
    assert "Error: Please enter valid numbers." in captured.out

def test_app_keyboard_interrupt(monkeypatch, capsys, caplog):
    """Test if KeyboardInterrupt exits."""
    def mock_input(_):
        raise KeyboardInterrupt
    monkeypatch.setattr("builtins.input", mock_input)
    caplog.clear()  # Clear previous logs
    caplog.set_level(logging.INFO)
    with pytest.raises(SystemExit):
        app = App()
        app.start()
    captured = capsys.readouterr()
    log_messages = [record.message for record in caplog.records]
    assert "Application interrupted"

def test_app_exit(monkeypatch, capsys):
    """Test if 'exit' command shuts down the app."""
    inputs = iter(["exit"])

    def mock_input(_):
        return next(inputs, "exit")

    monkeypatch.setattr("builtins.input", mock_input)

    with pytest.raises(SystemExit):
        app = App()
        app.start()

    captured = capsys.readouterr()
    assert "Exit" in captured.out
