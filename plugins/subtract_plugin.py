def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def register(command_handler):
    """Registers the 'subtract' command with the command handler."""
    print("DEBUG: Registering 'subtract' command in CommandHandler")  # Debugging print
    command_handler.register_command("subtract", subtract)