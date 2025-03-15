from calculator import Calculator

class CommandHandler:
    def __init__(self):
        """Map commands to calculator functions."""
        self.commands = {
            "add": Calculator.add,
            "subtract": Calculator.subtract,
            "multiply": Calculator.multiply,
            "divide": Calculator.divide,
        }

    def execute_command(self, command, num1, num2):
        """Executes a command."""
        if command not in self.commands:
            raise ValueError(f"Unknown command: {command}")
        return self.commands[command](num1, num2)