from calculator.operations import Operations

class Calculation:
    #Handles individual calculations.
    
    def __init__(self, operation: str, a: float, b: float):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = self._perform_operation()

    def _perform_operation(self) -> float:
        #Executes the requested operation and returns the result.
        operations_map = {
            "add": Operations.add,
            "subtract": Operations.subtract,
            "multiply": Operations.multiply,
            "divide": Operations.divide
        }
        return operations_map[self.operation](self.a, self.b)

    def __repr__(self) -> str:
        #Returns a string representation of the calculation.
        return f"{self.a} {self.operation} {self.b} = {self.result}"
