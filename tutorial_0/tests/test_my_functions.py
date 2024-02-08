import pytest
import time
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1, 4)
    assert result==5

def test_div_error():
    """
    This allows us to make sure that zerodiv error is raised
    """
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(10, 0)

def test_div_error2():
    """
    An example showing to ensure error is raised from definition
    """
    with pytest.raises(ValueError):
        my_functions.divide2(10, 2)

@pytest.mark.slow
def test_very_slow():
    time.sleep(3)
    res = my_functions.divide(10, 5)
    assert res == 2

@pytest.mark.skip(reason="This feature is WIP")
def test_add():
    assert my_functions.add(1, 2) == 3

@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    assert my_functions.divide(4, 6)