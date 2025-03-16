Michael Galanaugh
IS601 Midterm

# Calculator Application

## Overview
This project is an advanced Python-based calculator application designed to showcase my real-world abilities to code while utilizing Git/branching, REPL, and strong software engineering practices.  It integrates a robust REPL (Read-Eval-Print Loop) interface, a plugin system that loads on app initialization automatically, calculation history management using Pandas, and logging.

  [YouTube Video for Presentation](https://youtu.be/y2JEkWHDVeo)

## Features
- **Operations:** Supports arithmetic operations: add, subtract, multiply, and divide.
- **Plugins:** Dynamically loads new commands without modifying the core application.
- **Calculation History:** Uses Pandas to store and manage a history of calculations archived in a CSV file. Users can load or clear history
- **REPL Commands:** Provides additional commandsL:
  - `menu` – List available commands.
  - `history` – Display historical calculations.
  - `clear` – Clear all calculation history.
- **Dynamic Logging Configuration:** Logging is configured via environment variables and the `logging.conf` file. Users can adjust logging levels and output of the logging file as needed
- **Pytest, Pylint, Testing:** Achieves 95%+ test coverage using Pytest and 9.15/10+ code rating and maintains code quality with Pylint, adhering to PEP 8 standards.

## Architecture and Design Decisions

### Design Patterns
- **Simple Interface / Facade Pattern:**  
  The `Calculator` class provides a simplified interface for performing operations. History management and logging are performed by other Python modules (`calculation.py`, `calculations.py`, etc.).

  [Calculator implementation](https://github.com/mikeygman11/IS601_Midterm/tree/master/calculator)

- **Command Handler:**  
  The application employs a `CommandHandler` class to register and execute commands and extends functionality.

  [Command Handler](https://github.com/mikeygman11/IS601_Midterm/blob/master/app/__init__.py)
  
- **Factory Pattern:**  
  The `Calculation` instantiates new Calculation instances.
  The calculation history is maintained in the `Calculations` class
  [Calculations Class](https://github.com/mikeygman11/IS601_Midterm/blob/master/calculator/calculations.py)

### Plugin System
- **Dynamic Loading:**  
  Plugins are placed in the `plugins/` folder. The `load_plugins.py` module dynamically loads all plugin modules and calls their `register()` functions to register their commands with the `CommandHandler`

  - New operations can be added simply by creating a new plugin module (with a `register()` function) in the `plugins/` folder.
  [Plugins](https://github.com/mikeygman11/IS601_Midterm/tree/master/plugins)

### Calculation History Management
- **Pandas:**  
  The application uses the Pandas library to manage a history of calculations. Each calculation is saved in a CSV file (`logs/calculation_history.csv`) and the logging functionality writes to this csv.  
- **History Functions:**  
  Users can view, load, save, and clear calculation history through dedicated REPL commands. The `Calculations` class covers history management.
  [Calculations Class](https://github.com/mikeygman11/IS601_Midterm/blob/master/calculator/calculations.py)

### Logging Strategy
- **Logging Configuration:**  
  Logging is configured using a `logging.conf` file and environment variables in a .env file (which was excluded from the upload for obvious reasons.) You can change the logging level (e.g., INFO, DEBUG, ERROR) without modifying code.
- **Log File:**  
  Logs are written to `logs/app.log` with messages about warnings, messages, errors, etc
  The logging configuration is covered in `log/logging_setup.py`, which reads from `log/logging.conf`
  [Logging Setup](https://github.com/mikeygman11/IS601_Midterm/blob/master/log/logging_setup.py)

Environment variables are set by default and dynamically loaded when the program launches, but can be set to the user's preferences.
[Logging Config](https://github.com/mikeygman11/IS601_Midterm/blob/master/log/logging.conf)

[Logging Confifg and Auto-loading of Plugins](https://github.com/mikeygman11/IS601_Midterm/blob/master/plugins/load_plugins.py)

In command handler, I load env variables by default, but they can be changed in the program or in the .env file. 
[Environment Variable Code](https://github.com/mikeygman11/IS601_Midterm/blob/master/app/command_handler.py)

In the app initialization, I use try-catch blocks to run the calculator indefinetely unless you come across an issue with an unrecognized command (EAFP)

[Try-Catch](https://github.com/mikeygman11/IS601_Midterm/blob/master/app/__init__.py)

It can also be seen when loading plugins where I load the plugin and handle errors loading if there is an issue, rather than checking if the plugin exists first.
[Another Try-Catch](https://github.com/mikeygman11/IS601_Midterm/blob/master/app/__init__.py)

Finally, I implement LYBL in the divide function, when I check for division by 0 errors before executing.
[Division by 0](https://github.com/mikeygman11/IS601_Midterm/blob/master/plugins/divide_plugin.py)


## Setup and Installation


## Prerequisites
- **Python 3.8+**  
- **Pip**  
- **Virtual Environment (venv recommended)**  

## Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mikeygman11/IS601_CalcApp.git
   cd IS601_CalcApp
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

   - **On Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

   - **On Windows:**
     ```bash
     venv\Scripts\activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Application:**
   ```bash
   python main.py
   ```

5. **Run Commands for the Calculator:**
   - The command-line interface will provide options to:
     - Add
     - Subtract
     - Multiply
     - Divide
     - Show history (`history` command)
     - Clear history
     - Show menu
     - Exit the application  

   - The interface is interactive and user-friendly.
Start the app: python main.py
Perform operations: Use commands like add, subtract, multiply, divide.
Manage history: Use history to view, and clear to delete the calculator history.
Display commands: Use menu to list available commands.
Exit: Use exit to terminate the application.
## Example Usage

```cmd
Loaded environment variables.
Loaded 12 history records.

--- Welcome to Mike's calculator app ---
Arithmetic operations include: add, subtract, multiply, divide.
Other commands to choose from: history, clear, menu. Type exit to terminate the application

>>> add
Enter first number: 20
Enter second number: 5
History successfully saved to logs/calculation_history.csv
Result: 25.0

>>> divide
Enter first number: 454
Enter second number: 2
History successfully saved to logs/calculation_history.csv
Result: 227.0

>>> history

--- Calculation History ---
Calculation(20.0, 5.0, add)
Calculation(454.0, 2.0, divide)

>>> clear

Calculation history cleared.

>>> exit
Exit
```