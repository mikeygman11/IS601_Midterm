import sys
import logging
import logging.config
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
        print("DEBUG: Loading history on startup...")
        Calculations.load_history()

    def start(self):
        """Start the REPL."""
        print("Available commands:", list(self.command_handler.commands.keys()))
        print("Supported commands: add, subtract, multiply, divide, history, clear_history, menu")
        print("Type 'exit' at any prompt to quit.")
        
        try:
            while True:
                cmd_input = input(">>> ").strip().lower()
                if cmd_input == "exit":
                    logging.info("Application exiting.")
                    print("Exiting!")
                    sys.exit(0)
                elif cmd_input == "menu":
                    self.show_menu()
                    continue
                elif cmd_input == "history":
                    self.show_history()
                    continue
                elif cmd_input == "clear_history":
                    self.clear_history()
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
            print("\nGoodbye!")
            sys.exit(0)
        finally:
            logging.info("Shutting Down")

    def show_menu(self):
        """Display a menu of available commands."""
        print("\n--- REPL Menu ---")
        print("Commands:")
        for cmd in self.command_handler.commands.keys():
            print(f"  - {cmd}")
        print("  - history : View calculation history")
        print("  - clear_history : Delete calculation history")
        print("  - menu : Show this menu")
        print("  - exit : Exit the application\n")

    def show_history(self):
        """Display the calculation history using Pandas."""
        history_file = Calculations.history_file
        if os.path.exists(history_file):
            df = pd.read_csv(history_file)
            if df.empty:
                print("\nNo history found.")
            else:
                print("\n--- Calculation History ---")
                print(df)
        else:
            print("\nNo history found.")

    def clear_history(self):
        """Clear the calculation history."""
        Calculations.clear_history()
        print("\nCalculation history cleared.")

    def load_environment_variables(self):
        """Load environment variables into a dictionary."""
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

if __name__ == "__main__":
    app = App()
    app.start()
