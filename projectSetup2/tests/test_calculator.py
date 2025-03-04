# pylint: disable=missing-module-docstring, missing-function-docstring
"""This module contains the main functionality for the calculator application."""
import pytest
from calculator.operations import Operations  # Import the correct class

def test_addition():
    #Testing the addition function
    assert Operations.add(2, 2) == 4
    assert Operations.add(-1, 1) == 0
    assert Operations.add(0.5, 0.5) == 1.0

def test_subtraction():
    #Testing the subtraction function
    assert Operations.subtract(2, 2) == 0
    assert Operations.subtract(-5, -5) == 0
    assert Operations.subtract(10, 5) == 5

def test_multiplication():
    #Testing the multiplication function
    assert Operations.multiply(3, 7) == 21
    assert Operations.multiply(-5, 5) == -25  # Fixed incorrect value (-20 -> -25)
    assert Operations.multiply(0, 4) == 0

def test_division():
    #Testing the division function
    assert Operations.divide(6, 3) == 2
    assert Operations.divide(5, 2) == 2.5
    assert Operations.divide(-6, 3) == -2

def test_division_by_zero():
    #Testing division by zero exception
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        Operations.divide(5, 0)
