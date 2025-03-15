# App.py
from CommandHandler import CommandHandler
import sys

class App:
    def __init__(self):
        self.handler = CommandHandler()

    def start(self):
        print("Welcome to the Calculator REPL!")
        print("Supported commands: add, subtract, multiply, divide")
        print("Type 'exit' at any prompt to quit.")

        while True:
            command = input("Enter command: ").strip()
            if command.lower() == "exit":
                print("Goodbye!")
                sys.exit(0)

            inputs_str = input("Enter inputs (space separated): ").strip()
            if inputs_str.lower() == "exit":
                print("Goodbye!")
                sys.exit(0)

            args = inputs_str.split()
            try:
                # Convert the input strings to floats
                args = [float(arg) for arg in args]
            except ValueError:
                print("Error: All inputs must be numbers.")
                continue

            try:
                self.handler.execute_command(command, args)
            except Exception as e:
                print(f"Error: {e}")