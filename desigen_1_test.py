import math
import pytest

def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_factorial():
    assert factorial(5) == 120
    assert factorial(1) == math.factorial(1)
    assert factorial(0) == math.factorial(0)
    assert factorial(3) == math.factorial(3)
    assert factorial(1500) == math.factorial(1500)
    



def test_factorial_negative_input():
    with pytest.raises(ValueError):
        factorial(-1)
        factorial(-5)
    
   