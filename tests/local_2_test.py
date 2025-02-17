


import pytest


def add(a, b):
    return a + b

def test_add():
    a = 0.1
    b = 0.2
    assert pytest.approx(add(a, b)) == 0.3
