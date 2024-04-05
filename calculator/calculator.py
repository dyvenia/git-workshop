import math


def add(x, y):
    """Returns the sum of x and y."""
    return x + y


def multiply(x, y):
    """Returns the product of x and y."""
    return x * y


def divide(x, y):
    """Returns the result of dividing x by y."""
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"


def subtract(x, y):
    """Returns the difference between x and y."""
    return x - y


def exponentiate(x, y):
    """Returns x raised to the power of y."""
    return x**y


def root_square(x):
    """Returns the square root of x."""
    return math.sqrt(x)
