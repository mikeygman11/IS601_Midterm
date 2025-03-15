# tests/test_calculator.py
import pytest
from app.Calculator import Calculator

def test_add():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5, f"Expected 2 + 3 to equal 5, but got {result}"

def test_subtract():
    calc = Calculator()
    result = calc.subtract(10, 4)
    assert result == 6, f"Expected 10 - 4 to equal 6, but got {result}"

def test_multiply():
    calc = Calculator()
    result = calc.multiply(4, 5)
    assert result == 20, f"Expected 4 * 5 to equal 20, but got {result}"

def test_divide():
    calc = Calculator()
    result = calc.divide(20, 4)
    assert result == 5, f"Expected 20 / 4 to equal 5, but got {result}"

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)