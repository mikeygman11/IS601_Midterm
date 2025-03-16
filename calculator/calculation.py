"""
This module defines the Calculation class, which represents a calculation
in the calculator, including operands and the operation performed.
"""
from decimal import Decimal
from typing import Callable

class Calculation:
    """Calculation class for calculator operations"""
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod    
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """create a new function"""
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        """Perform the stored calculation and return the result."""
        return self.operation(self.a, self.b)

    def __repr__(self):
        """Return a string representation of the calculation."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
