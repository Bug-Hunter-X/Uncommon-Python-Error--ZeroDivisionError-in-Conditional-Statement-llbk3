def function_with_uncommon_error(a, b):
    if a == 0:
        return float('inf')  # Return positive infinity
        # or raise a more descriptive exception:
        # raise ZeroDivisionError("Cannot divide by zero")
    return a + b