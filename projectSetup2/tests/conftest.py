"""This module contains the main functionality for the calculator application."""
import pytest
from calculator.calculations import Calculation
from calculator.history import CalculationHistory

@pytest.fixture
def sample_calculations():
    """Provides sample calculations for testing."""
    CalculationHistory.clear_history()
    CalculationHistory.add_calculation(Calculation("add", 3, 2))
    CalculationHistory.add_calculation(Calculation("multiply", 4, 2))
    return CalculationHistory
