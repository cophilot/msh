def assert_true(value, raise_assertion_error=True):
    if value:
        return True

    if raise_assertion_error:
        raise AssertionError("Expected True but got False")
    return False


def assert_false(value, raise_assertion_error=True):
    if not value:
        return True

    if raise_assertion_error:
        raise AssertionError("Expected False but got True")
    return False


def assert_equal(a, b, raise_assertion_error=True):
    if a == b:
        return True

    if raise_assertion_error:
        raise AssertionError(f"Expected {a} but got {b}")
    return False
