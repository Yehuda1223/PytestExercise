from unittest.mock import patch 


def check_reactor_temperature(temperature_celsius):       
    """
    Checks whether temperature is above max_temperature
    and returns a status.
    """
    from reactor import max_temperature 
    if temperature_celsius > max_temperature:
        status = 1
    else:
        status = 0
    return status

@patch('reactor.max_temperature', 100)
def test_check_reactor_temperature():
    assert check_reactor_temperature(101) == 1
    assert check_reactor_temperature(99) == 0
    assert check_reactor_temperature(100) == 0

