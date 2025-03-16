import pytest
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal

@pytest.fixture(autouse=True)
def clear_history():
    """Clear the history before each test to ensure test isolation."""
    Calculations.clear_history()

def test_add_calculation():
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal(5), Decimal(3), add)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1
    assert Calculations.get_history()[0] == calc

def test_get_history():
    """Test retrieving the calculation history."""
    calc1 = Calculation(Decimal(2), Decimal(2), multiply)
    calc2 = Calculation(Decimal(10), Decimal(5), divide)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    history = Calculations.get_history()
    assert len(history) == 2
    assert history == [calc1, calc2]

def test_clear_history():
    """Test clearing the calculation history."""
    calc = Calculation(Decimal(4), Decimal(2), subtract)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

def test_get_latest():
    """Test retrieving the latest calculation."""
    assert Calculations.get_latest() is None  # Ensure None is returned when no history exists
    calc1 = Calculation(Decimal(3), Decimal(1), add)
    calc2 = Calculation(Decimal(7), Decimal(4), subtract)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    assert Calculations.get_latest() == calc2  # Latest should be last added

def test_find_by_operation():
    """Test finding calculations by operation name."""
    calc1 = Calculation(Decimal(6), Decimal(2), divide)
    calc2 = Calculation(Decimal(5), Decimal(3), add)
    calc3 = Calculation(Decimal(8), Decimal(4), divide)

    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    Calculations.add_calculation(calc3)

    division_calculations = Calculations.find_by_operation("divide")
    assert len(division_calculations) == 2
    assert calc1 in division_calculations
    assert calc3 in division_calculations

def test_find_by_operation_no_match():
    """Test searching for an operation that doesn't exist."""
    calc = Calculation(Decimal(2), Decimal(2), multiply)
    Calculations.add_calculation(calc)
    assert Calculations.find_by_operation("subtract") == []
