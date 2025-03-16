"""Testing calculator program"""
import sys
import os
from decimal import Decimal
import pytest
from calculator import Calculator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_calculator_add():
    """Test Calculator's add method."""
    assert Calculator.add(Decimal(2), Decimal(3)) == Decimal(5)

def test_calculator_subtract():
    """Test Calculator's subtract method."""
    assert Calculator.subtract(Decimal(5), Decimal(2)) == Decimal(3)

def test_calculator_multiply():
    """Test Calculator's multiply method."""
    assert Calculator.multiply(Decimal(3), Decimal(4)) == Decimal(12)

def test_calculator_divide():
    """Test Calculator's divide method."""
    assert Calculator.divide(Decimal(10), Decimal(2)) == Decimal(5)

def test_calculator_divide_by_zero():
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(Decimal(10), Decimal(0))
