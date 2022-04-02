from errors import AssertionFailed

def assertEq(*values):
    valueToCheck = values[0]

    for index, value in enumerate(values[1:]):
        if value != valueToCheck:
            raise AssertionFailed(values, index+1, "==")

assertEq(5, 2+4)
