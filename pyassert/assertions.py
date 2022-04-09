from .errors import AssertionFailed

def assert_(value):
    """
    Asserts that the value is true.
    If the value is false, an AssertionFailed exception is raised.

    value: the value to check
    """
    if not value:
        raise AssertionFailed(value, "True", "!=")

def assert_eq(left, right):
    """
    Asserts that the left value is equal to the right value.
    If the left value is not equal to the right value, an AssertionFailed exception is raised.

    left: left value
    right: right value
    """
    if not left == right:
        raise AssertionFailed(left, right, "==")

def assert_ne(left, right):
    """
    Asserts that the left value is not equal to the right value.
    If the left value is equal to the right value, an AssertionFailed exception is raised.

    left: left value
    right: right value
    """
    if not left != right:
        raise AssertionFailed(left, right, "!=")

def assert_gt(left, right):
    """
    Asserts that the left value is greater than the right value.
    If the left value is not greater than the right value, an AssertionFailed exception is raised.

    left: left value
    right: right value
    """
    if not left > right:
        raise AssertionFailed(left, right, ">")

def assert_lt(left, right):
    """
    Asserts that the left value is lower than the right value.
    If the left value is not lower than the right value, an AssertionFailed exception is raised.

    left: left value
    right: right value
    """
    if not left < right:
        raise AssertionFailed(left, right, "<")

def assert_ge(left, right):
    """
    Asserts that the left value is greater or equal to the right value.
    If the left value is not greater or equal to the right value, an AssertionFailed exception is raised.

    left: left value
    right: right value
    """
    if not left >= right:
        raise AssertionFailed(left, right, ">=")

def assert_le(left, right):
    """
    Asserts that the left value is lower or equal to the right value.
    If the left value is not lower or equal to the right value, an AssertionFailed exception is raised.

    left: left value
    right: right value
    """
    if not left <= right:
        raise AssertionFailed(left, right, "<=")
