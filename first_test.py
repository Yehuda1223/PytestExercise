def add (x, y):
    return x + y


def test_add():
    assert add(1, 2) == 3
    assert add(2, 2) == 4
    assert add(3, 2) == 5
    
    
def minus (x, y):
    return x - y


def test_minus(): 
    assert minus(1, 2) == -1
    assert minus(2, 2) == 0
    assert minus(3, 2) == 1
    
    
def multiply (x, y):
    return x * y

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(2, 2) == 4
    assert multiply(3, 2) == 6
    