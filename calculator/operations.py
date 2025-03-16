"""
This module contains basic arithmetic operations: add, subtract, multiply, and divide.
"""
from decimal import Decimal
def add(a: Decimal, b: Decimal) -> Decimal:
    """add function for two numbers"""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """subtract function for 2 numbers"""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """multiply function for 2 numbers"""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """divide function for two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
