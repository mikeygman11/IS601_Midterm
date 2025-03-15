# app/CommandHandler.py
from app.Calculator import Calculator

class CommandHandler:
    def __init__(self):
        self.calculator = Calculator()
        self.commands = {
            "add": self.add,
            "subtract": self.subtract,
            "multiply": self.multiply,
            "divide": self.divide
        }

    def execute_command(self, command, args):
        command = command.lower()
        if command not in self.commands:
            raise KeyError(f"Command '{command}' not recognized.")
        result = self.commands[command](*args)
        if result is not None:
            print(result)

    def add(self, a, b):
        return self.calculator.add(a, b)

    def subtract(self, a, b):
        return self.calculator.subtract(a, b)

    def multiply(self, a, b):
        return self.calculator.multiply(a, b)

    def divide(self, a, b):
        return self.calculator.divide(a, b)