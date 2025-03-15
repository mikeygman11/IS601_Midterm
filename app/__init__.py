from log.logging_setup import configure_logging  # Import from log folder
from app.CommandHandler import CommandHandler
import sys
import logging
import logging.config
import os
from dotenv import load_dotenv
from plugins.loadPlugins import load_plugins
from log.logging_setup import configure_logging

class App:
    def __init__(self):
        """Initialize the application with logging, environment variables, and command handling."""
        os.makedirs('logs', exist_ok=True)  # Ensure the logs directory exists
        configure_logging(self)  # Set up logging
        self.logger = logging.getLogger(__name__)

        load_dotenv()  # Load environment variables from .env file
        self.settings = self.load_environment_variables()  
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')

        self.command_handler = CommandHandler()
        load_plugins(self.command_handler)

    def start(self):
        print("\nDEBUG: Available commands:", list(self.command_handler.commands.keys()))  # Debugging print

        self.logger.info("Application started. Type 'exit' to exit.")       
        print("Supported commands: add, subtract, multiply, divide")
        print("Type 'exit' at any prompt to quit.")

        try:
            while True:
                cmd_input = input(">>> ").strip().lower()
                if cmd_input == "exit":
                    logging.info("Application exit.")
                    print("Exiting!")
                    sys.exit(0)

                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    result = self.command_handler.execute_command(cmd_input, num1, num2)
                    print(f"Result: {result}")
                    logging.info(f"Executed {cmd_input} with inputs {num1} and {num2}: Result {result}")

                except ValueError:
                    print("Error: Please enter valid numbers.")
                    logging.warning(f"Invalid number input for command {cmd_input}")

                except KeyError:
                    print(f"Error: Unknown command '{cmd_input}'")
                    logging.error(f"Unknown command entered: {cmd_input}")

        except KeyboardInterrupt:
            logging.info("Application interrupted. Exiting")
            print("\nGoodbye!")
            sys.exit(0)

        finally:
            logging.info("Shutting Down")

    def load_environment_variables(self):
        """Loads environment variables into the settings dictionary."""
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings
    


if __name__ == "__main__":
    # print("DEBUG: main.py execution started")  # Debug print
    app = App()
    app.start()