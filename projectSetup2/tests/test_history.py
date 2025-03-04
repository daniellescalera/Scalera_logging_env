# pylint: disable=missing-module-docstring, missing-function-docstring
#testing all the history, when user selects history it will show
#unit tests for all calculation history

def test_add_and_retrieve_calculation(sample_calculations):
    #Test storing and retrieving calculations.
    last_calc = sample_calculations.get_last_calculation()
    assert last_calc is not None
    assert last_calc.operation == "multiply"
    assert last_calc.result == 8

def test_clear_history(sample_calculations):
    #Test clearing history.
    sample_calculations.clear_history()
    assert sample_calculations.get_last_calculation() is None
