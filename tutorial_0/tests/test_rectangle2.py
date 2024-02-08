import pytest

def test_area2(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
