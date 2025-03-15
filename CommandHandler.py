# CommandHandler.py
from decimal import Decimal
from typing import List

class CommandHandler:
    def __init__(self):
        # A dictionary mapping command names (strings) to handler methods.
        self.commands = {
            "add": self.add_command,
            "subtract": self.subtract_command,
            "multiply": self.multiply_command,
            "divide": self.divide_command
        }

    def handle_command(self, command_name: str, args: List[Decimal]) -> Decimal:
        """
        Dispatches the given command to the appropriate handler.
        Args:
            command_name: The string name of the command (e.g., 'add', 'subtract').
            args: A list of Decimal arguments to the command.
        Returns:
            The result of the arithmetic operation as a Decimal.
        Raises:
            ValueError: If the command is unknown or not enough arguments are provided.
        """
        # Check if the command is known
        if command_name not in self.commands:
            raise ValueError(f"Unknown command: {command_name}")

        # Ensure at least two arguments are provided for binary operations
        if len(args) < 2:
            raise ValueError("Must provide at least two numbers.")

        # Dispatch to the corresponding method
        return self.commands[command_name](args[0], args[1])

    def add_command(self, a: Decimal, b: Decimal) -> Decimal:
        """Return the sum of a and b."""
        return a + b

    def subtract_command(self, a: Decimal, b: Decimal) -> Decimal:
        """Return the difference of a and b."""
        return a - b

    def multiply_command(self, a: Decimal, b: Decimal) -> Decimal:
        """Return the product of a and b."""
        return a * b

    def divide_command(self, a: Decimal, b: Decimal) -> Decimal:
        """Return the quotient of a and b, raising an error if b is zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b