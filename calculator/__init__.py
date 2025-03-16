"""__init__.py to declare a Calculator class"""
from decimal import Decimal
from typing import Callable
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculator:
    """initializing the Calculator class that performs various operations"""
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """performing each calculation"""
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """add method for Calc"""
        return Calculator._perform_operation(a, b, add)
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """subtract method for calc"""
        return Calculator._perform_operation(a, b, subtract)
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """multiply method for calc"""
        return Calculator._perform_operation(a, b, multiply)
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """divide method for calc"""
        return Calculator._perform_operation(a, b, divide)
