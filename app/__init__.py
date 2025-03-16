"""Starting up application"""
import sys
import logging
import os
from log.logging_setup import configure_logging
from app.command_handler import CommandHandler
from dotenv import load_dotenv
from plugins.load_plugins import load_plugins
from calculator.calculations import Calculations
import pandas as pd

class App:
    """Main application class that handles REPL, history, and configuration."""

    def __init__(self):
        """Initialize the App."""
        os.makedirs('logs', exist_ok=True)
        configure_logging(self)
        self.logger = logging.getLogger(__name__)
        
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')

        self.command_handler = CommandHandler()
        load_plugins(self.command_handler)
        
        # Load calculation history from file
        Calculations.load_history()

    def start(self):
        """Start the REPL."""
        print("\n--- Welcome to Mike's calculator app ---")
        print("Arithmetic operations include: add, subtract, multiply, divide.")
        print("Other commands to choose from: history, clear, menu. Type exit to terminate the application")
        try:
            while True:
                cmd_input = input(">>> ").strip().lower()
                if cmd_input == "exit":
                    logging.info("Application exiting.")
                    print("Exit")
                    sys.exit(0)

                elif cmd_input in ["menu", "history", "clear"]:
                    self.command_handler.execute_command(cmd_input)
                    continue

                elif cmd_input not in self.command_handler.commands:
                    logging.error("Unknown command entered: %s", cmd_input)
                    print(f"Error: Unknown command '{cmd_input}'")
                    continue

                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    result = self.command_handler.execute_command(cmd_input, num1, num2)
                    print(f"Result: {result}")
                    logging.info("Executed %s with inputs %s and %s: Result %s", cmd_input, num1, num2, result)
                except ValueError:
                    logging.warning("Invalid number input for command %s", cmd_input)
                    print("Error: Please enter valid numbers.")
        except KeyboardInterrupt:
            logging.info("Application interrupted")
            print("\nApplication interrupted")
            sys.exit(0)
        finally:
            logging.info("Shutting Down")

    def load_environment_variables(self):
        """Load environment variables into a dictionary."""
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

if __name__ == "__main__":
    app = App()
    app.start()
