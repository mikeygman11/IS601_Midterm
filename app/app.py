import sys
from app.CommandHandler import CommandHandler

class App:
    def __init__(self):
        """Initialize REPL with command handling."""
        self.command_handler = CommandHandler()

    def start(self):
        """Run the REPL loop."""
        print("🧮 Welcome to the Calculator REPL!")
        print("Type 'menu' to see available commands. Type 'exit' to quit.")

        while True:
            command = input("Enter command: ").strip().lower()
            if command == "exit":
                print("Goodbye!")
                sys.exit(0)

            elif command == "menu":
                print("Available Commands: add, subtract, multiply, divide")
                continue

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = self.command_handler.execute_command(command, num1, num2)
                print("Result:", result)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    App().start()