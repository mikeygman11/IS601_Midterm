"""
Defines the CommandHandler class, which allows registering and executing
commands dynamically in the REPL environment.
"""
import os
import logging
import dotenv
from calculator.calculations import Calculations

class CommandHandler:
    """Handles registering and executing commands in the REPL."""
    
    def __init__(self):
        self.commands = {}
        self.logger = logging.getLogger(__name__)
        self.load_environment_variables()
        self.register_command("history", self.show_history)
        self.register_command("clear", self.clear_history)
        self.register_command("menu", self.show_menu)
        self.register_command("load_env", self.load_environment_variables)

    def register_command(self, command_name, function):
        """Registers a command to be callable in the app"""
        self.commands[command_name] = function


    def execute_command(self, command, *args):
        """Executes a command if registered."""
        if command in self.commands:
            func = self.commands[command]

            if callable(func):
                expected_arg_count = func.__code__.co_argcount
                
                # If function takes no arguments, call it without arguments
                if expected_arg_count == 0:
                    return func()
                
                # Otherwise, execute with expected number of arguments
                return func(*args[:expected_arg_count])
        
        raise KeyError(f"Unknown command: {command}")
    def show_history(self):
        """Displays the stored calculation history."""
        history = Calculations.get_history()
        if history:
            print("\n--- Calculation History ---")
            for calc in history:
                print(calc)
        else:
            print("\nNo history found.")
        self.logger.info("Displayed calculation history")

    def clear_history(self):
        """Clears stored calculation history."""
        Calculations.clear_history()
        print("\nCalculation history cleared.")
        self.logger.info("Calculation history cleared")

    def show_menu(self):
        """Displays a menu of available commands."""
        menu = (
            "\n--- Calculator Menu ---\n"
            "Commands:\n"
            "- add\n"
            "- subtract\n"
            "- multiply\n"
            "- divide\n"
            "- history\n"
            "- clear_history\n"
            "- menu\n"
            "- load_env\n"
            "- exit\n"
        )
        print(menu)

    def load_environment_variables(self):
        """Loads environment variables from .env file."""
        dotenv.load_dotenv()
        self.settings = {key: value for key, value in os.environ.items()}
        self.logger.info("Environment variables loaded.")
        print("\nLoaded environment variables.")
