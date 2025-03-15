from log.logging_setup import configure_logging  # Import from log folder
from app.CommandHandler import CommandHandler
import sys
import logging

class App:
    def __init__(self):
        print("TEST")
        configure_logging()
        self.logger = logging.getLogger(__name__)
        self.command_handler = CommandHandler()

    def start(self):
        self.logger.info("Calculator REPL started.")
        print("Welcome to the Calculator REPL!")

        while True:
            command = input("Enter command: ").strip().lower()
            if command == "exit":
                self.logger.info("Exiting REPL.")
                print("Goodbye!")
                sys.exit(0)

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = self.command_handler.execute_command(command, num1, num2)
                print("Result:", result)
                self.logger.info(f"Performed {command} on {num1}, {num2}: {result}")
            except Exception as e:
                self.logger.error(f"Error: {e}")
                print(f"Error: {e}")

if __name__ == "__main__":
    print("DEBUG: main.py execution started")  # Debug print
    app = App()  # Constructor should print debug message
    app.start()