class AssertionFailed(Exception):
    
    def __init__(self, values, failedIndex, operand):
        self.values = values
        self.failedIndex = failedIndex
        self.operand = operand

    def __str__(self):
        return f"""Assertion failed:
________________________________________________________________________
not {self.values[0]} {self.operand} {self.values[self.failedIndex]}
________________________________________________________________________
Failed at index {self.failedIndex}
        """
