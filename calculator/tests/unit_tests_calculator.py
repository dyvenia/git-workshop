from calculator import add, multiply, divide, subtract, exponentiate, square_root


def test_addition():
    assert add(5, 3) == 8
    assert add(0, 0) == 0
    assert add(-5, 5) == 0


def test_multiplication():
    assert multiply(4, 6) == 24
    assert multiply(0, 10) == 0
    assert multiply(-3, 7) == -21


def test_division():
    assert divide(8, 2) == 4.0
    assert divide(10, 5) == 2.0
    assert divide(7, 0) == "Error: Division by zero"


def test_subtraction():
    assert subtract(10, 7) == 3
    assert subtract(5, 5) == 0
    assert subtract(7, 10) == -3


def test_exponentiation():
    assert exponentiate(2, 3) == 8
    assert exponentiate(5, 0) == 1
    assert exponentiate(3, -2) == 1 / 9


def test_square_root():
    assert square_root(4) == 2
    assert square_root(25) == 5
    assert square_root(9) == 3
