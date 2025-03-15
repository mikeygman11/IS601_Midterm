import pytest
from decimal import Decimal
import sys
import os
# Ensure the project root is in sys.path so calculator can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plugins.add_plugin import add
from plugins.subtract_plugin import subtract
from plugins.multiply_plugin import multiply
from plugins.divide_plugin import divide

from calculator import Calculator  # Import Calculator from the calculator package


def test_add():
    assert add(5, 3) == 8
    assert add(-2, 4) == 2
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(5, 8) == -3
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-3, 6) == -18
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-12, 3) == -4
    assert divide(9, 3) == 3

# ✅ Error Handling
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)