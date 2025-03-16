"""Plugin for displaying available commands in REPL menu."""
def menu():
    """Displays a menu of available commands."""
    menu_text = (
        "\n--- REPL Menu ---\n"
        "Commands:\n"
        "- add\n"
        "- subtract\n"
        "- multiply\n"
        "- divide\n"
        "- history\n"
        "- clear_history\n"
        "- menu\n"
        "- load_env\n"
        "- exit\n"
    )
    print(menu_text)

def register(command_handler):
    """Register the menu command."""
    command_handler.register_command("menu", menu)
