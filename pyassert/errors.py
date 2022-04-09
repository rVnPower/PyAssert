class AssertionFailed(Exception):
    
    def __init__(self, left, right, operand):
        self.left = left
        self.right = right
        self.operand = operand

    def __str__(self):
        return f"""Assertion failed:
________________________________________________________________________
(left {self.operand} right)
left: `{self.left}`
right: `{self.right}`
________________________________________________________________________
        """
