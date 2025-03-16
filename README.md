Michael Galanaugh
IS601 Midterm

# Calculator Application

## Overview
This project is an advanced Python-based calculator application designed to showcase my real-world abilities to code while utilizing Git/branching, REPL, and strong software engineering practices.  It integrates a robust REPL (Read-Eval-Print Loop) interface, a plugin system that loads on app initialization automatically, calculation history management using Pandas, and logging.

## Features
- **Operations:** Supports arithmetic operations: add, subtract, multiply, and divide.
- **Plugins:** Dynamically loads new commands without modifying the core application.
- **Calculation History:** Uses Pandas to store and manage a history of calculations archived in a CSV file. Users can load or clear history
- **REPL Commands:** Provides additional commandsL:
  - `menu` – List available commands.
  - `history` – Display historical calculations.
  - `clear_history` – Clear all calculation history.
- **Dynamic Logging Configuration:** Logging is configured via environment variables and the `logging.conf` file. Users can adjust logging levels and output of the logging file as needed
- **Pytest, Pylint, Testing:** Achieves 95%+ test coverage using Pytest and 9.15/10+ code rating and maintains code quality with Pylint, adhering to PEP 8 standards.

## Architecture and Design Decisions

### Design Patterns
- **Simple Interface / Facade Pattern:**  
  The `Calculator` class provides a simplified interface for performing operations. History management and logging are performed by other Python modules (`calculation.py`, `calculations.py`, etc.).
  
- **Command Handler:**  
  The application employs a `CommandHandler` class to register and execute commands and extends functionality.
  
- **Factory Pattern:**  
  The `Calculation` instantiates new Calculation instances.
  The calculation history is maintained in the `Calculations` class

### Plugin System
- **Dynamic Loading:**  
  Plugins are placed in the `plugins/` folder. The `load_plugins.py` module dynamically loads all plugin modules and calls their `register()` functions to register their commands with the `CommandHandler`

  - New operations can be added simply by creating a new plugin module (with a `register()` function) in the `plugins/` folder.

### Calculation History Management
- **Pandas:**  
  The application uses the Pandas library to manage a history of calculations. Each calculation is saved in a CSV file (`logs/calculation_history.csv`) and the logging functionality writes to this csv.  
- **History Functions:**  
  Users can view, load, save, and clear calculation history through dedicated REPL commands. The `Calculations` class covers history management.

### Logging Strategy
- **Logging Configuration:**  
  Logging is configured using a `logging.conf` file and environment variables in a .env file (which was excluded from the upload for obvious reasons.) You can change the logging level (e.g., INFO, DEBUG, ERROR) without modifying code.
- **Log File:**  
  Logs are written to `logs/app.log` with messages about warnings, messages, errors, etc
  The logging configuration is covered in `log/logging_setup.py`, which reads from `log/logging.conf`

## Setup and Installation

### Prerequisites
- **Python 3.8+**  
- **Pip**  
- **Virtual Environment (venv recommended)**

### Installation Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mikeygman11/IS601_CalcApp.git
   cd IS601_CalcApp
2. **Create Virtual Env:**
python -m venv venv
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
3. **Install Needed Dependencies:**
pip install -r requirements.txt
4. **Start the App - run python main.py**
python main.py
5. **Run commands for calculator:**
You will be given options to add, subtract, multiply, divide, show history (history command), clear, menu, exit
The command line is interactive and responsive

Start the app: python main.py
Perform operations: Use commands like add, subtract, multiply, divide.
Manage history: Use history to view, and clear_history to delete the calculator history.
Display commands: Use menu to list available commands.
Exit: Use exit to terminate the application.

6. **Example Usage"**

Enter first number: 45
Enter second number: 3
History successfully saved to logs/calculation_history.csv
Result: 48.0

>>> history

--- Calculation History ---
      a    b operation  result
0  45.0  3.0       add    48.0