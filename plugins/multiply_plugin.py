def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def register(command_handler):
    """Registers the 'multiply' command with the command handler."""
    print("DEBUG: Registering 'multiply' command in CommandHandler")  # Debugging print
    command_handler.register_command("multiply", multiply)