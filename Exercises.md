### Basic level tasks

The repository you are currently in has a simple Python application inside it, which is a calculator. The application code can be found in the `calculator/calculator.py` directory. You have been assigned a user story for sprint planning to add additional functions to the calculator. So far, we have 4 functions that allow us to add, divide, multiply and subtract. Our client asks us to add two features:
- Exponentiating - Taking the arguments `x` as the base of the power and `y` as the exponent
- Square root - Taking only one argument `x` and calculating only the second degree root

Remember to add tests and docstings to these functions later.

**If you don't want to come up with these solutions yourself, the Answers section contains all the necessary changes to the files**

#### Step by step instructions

1. Clone repository. (If you have colonized the repository on your computer, you can skip this step)

2. Create your branch where you will add changes.

3. Add changes to all files. (Check the Answers tab for a list of files that need to be changed)

4. Sort your commits.

5. Test the code 
    - Go to `calculator/tests/` and run `pytest unit_tests_calculator.py`. If you don't have pytest install it using `pip install pytest`

6. Push changes to github.

7. Create a pull request and select `djagoda881` as reviewer.

### Medium level tasks

#### Step by step instructions

1. Fork the repository.

2. Create your branch where you will add changes.

3. Add changes to all files. (Check the Answers tab for a list of files that need to be changed)

4. Sort your commits.

5. Test the code 
    - Go to `calculator/tests/` and run `pytest unit_tests_calculator.py`. If you don't have pytest install it using `pip install pytest`

6. Push changes to github.

7. Create a pull request to `main` branch and select `djagoda881` as reviewer.
### Answers

```python
# calculator/calculator.py

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
    return x ** y

def square_root(x):
    """Returns the square root of x."""
    return math.sqrt(x)

```

```python
# calculator/__init__.py

from .calcurator import add, subtract, divide, multiply, exponentiate, square_root

```

```python
# calculator/tests/unit_tests_calculator.py

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
    assert exponentiate(3, -2) == 1/9
    
def test_square_root():
    assert square_root(4) == 2
    assert square_root(25) == 5
    assert square_root(9) == 3
```