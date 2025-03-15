def divide(a, b):
    """Returns the quotient of two numbers, handling division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def register(command_handler):
    """Registers the 'divide' command with the command handler."""
    print("DEBUG: Registering 'divide' command in CommandHandler")  # Debugging print
    command_handler.register_command("divide", divide)