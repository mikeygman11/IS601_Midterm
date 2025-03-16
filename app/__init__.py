import sys
import logging
import os
from log.logging_setup import configure_logging
from app.command_handler import CommandHandler
from dotenv import load_dotenv
from plugins.load_plugins import load_plugins

class App:
    """Instantiating the App class"""
    def __init__(self):
        """Constructor for App class"""
        os.makedirs('logs', exist_ok=True)
        configure_logging(self)  # Updated logging setup
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        load_plugins(self.command_handler)

    def start(self):
        """Start the app"""
        print("Available commands:", list(self.command_handler.commands.keys()))
        print("Supported commands: add, subtract, multiply, divide")
        print("Type 'exit' at any prompt to quit.")
        
        try:
            while True:
                cmd_input = input(">>> ").strip().lower()
                if cmd_input == "exit":
                    logging.info("Application interrupted")
                    print("Exiting!")
                    sys.exit(0)
                
                if cmd_input not in self.command_handler.commands:
                    print(f"Error: Unknown command '{cmd_input}'")
                    logging.error(f"Unknown command entered: {cmd_input}")
                    continue  # Move to next input loop
                
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    result = self.command_handler.execute_command(cmd_input, num1, num2)
                    print(f"Result: {result}")
                    logging.info(f"Executed {cmd_input} with inputs {num1} and {num2}: Result {result}")
                except ValueError:
                    print("Error: Please enter valid numbers.")
                    logging.warning(f"Invalid number input for command {cmd_input}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)
        finally:
            logging.info("Shutting Down")

    def load_environment_variables(self):
        """Loads environment variables into the settings dictionary."""
        settings = {key: value for key, value in os.environ.items()}
        return settings

if __name__ == "__main__":
    app = App()
    app.start()
