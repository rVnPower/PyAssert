from errors import AssertionFailed

def assert_eq(left, right):
    if not left == right:
        raise AssertionFailed(left, right, "==")

def assert_ne(left, right):
    if not left != right:
        raise AssertionFailed(left, right, "!=")

def assert_gt(left, right):
    if not left > right:
        raise AssertionFailed(left, right, ">")

def assert_lt(left, right):
    if not left < right:
        raise AssertionFailed(left, right, "<")

def assert_ge(left, right):
    if not left >= right:
        raise AssertionFailed(left, right, ">=")

def assert_le(left, right):
    if not left <= right:
        raise AssertionFailed(left, right, "<=")
