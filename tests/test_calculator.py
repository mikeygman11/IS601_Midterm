import pytest
from decimal import Decimal
import sys
import os

# Ensure the project root is in sys.path so calculator can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import Calculator  # Import Calculator from the calculator package


def test_add():
    """Test the addition function."""
    result = Calculator.add(Decimal("2"), Decimal("3"))
    assert result == Decimal("5"), f"Expected 5, got {result}"


def test_subtract():
    """Test the subtraction function."""
    result = Calculator.subtract(Decimal("10"), Decimal("4"))
    assert result == Decimal("6"), f"Expected 6, got {result}"


def test_multiply():
    """Test the multiplication function."""
    result = Calculator.multiply(Decimal("3"), Decimal("4"))
    assert result == Decimal("12"), f"Expected 12, got {result}"


def test_divide():
    """Test the division function."""
    result = Calculator.divide(Decimal("20"), Decimal("4"))
    assert result == Decimal("5"), f"Expected 5, got {result}"


def test_divide_by_zero():
    """Test division by zero raises an error."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(Decimal("10"), Decimal("0"))