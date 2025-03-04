
from typing import List
from calculator.calculations import Calculation

class CalculationHistory:
    #manages the history of the calculations. 
    _history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Stores a calculation in history."""
        cls._history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        #Returns the last calculation performed.
        if cls._history:
            return cls._history[-1]
        return None

    @classmethod
    def clear_history(cls):
        #Clears all calculation history.
        cls._history.clear()
