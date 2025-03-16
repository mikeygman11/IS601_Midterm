"""
This module manages a history of calculations using Pandas.
Calculations are stored in a CSV file so that the history persists across sessions.
"""
import pandas as pd
import os
from typing import List
from calculator.calculation import Calculation

class Calculations:
    """Class to manage calculation history using Pandas."""
    history: List[Calculation] = []
    history_file = "logs/calculation_history.csv"

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history and save it to CSV."""
        print("DEBUG: Adding calculation to history.")
        cls.history.append(calculation)
        cls.save_history()

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Return the current calculation history as a list."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history and delete the CSV file."""
        cls.history.clear()
        if os.path.exists(cls.history_file):
            os.remove(cls.history_file)

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if no history exists."""
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Return a list of calculations matching the given operation name."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]

    @classmethod
    def save_history(cls):
        """Save calculation history to CSV using Pandas."""
        if cls.history:
            data = []
            for calc in cls.history:
                try:
                    result = calc.perform()
                except ValueError as e:
                    result = None  # Record None if the calculation fails (e.g. division by zero)
                data.append({
                    "a": calc.a, 
                    "b": calc.b, 
                    "operation": calc.operation.__name__, 
                    "result": result
                })
            df = pd.DataFrame(data)
            os.makedirs("logs", exist_ok=True)
            df.to_csv(cls.history_file, index=False)
            print(f"History successfully saved to {cls.history_file}")
        else:
            print("No calculations to save.")


    @classmethod
    def load_history(cls):
        """Load calculation history from CSV using Pandas."""
        if os.path.exists(cls.history_file):
            df = pd.read_csv(cls.history_file)
            if df.empty:
                print("DEBUG: History file is empty.")
            else:
                # For simplicity, we won't reconstruct Calculation objects.
                print(f"DEBUG: Loaded {len(df)} history records.")
            return df
        else:
            print("DEBUG: No history file found.")
            return None
