import math
import pytest
import source.shapes as shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)

def test_area():
    rec = shapes.Rectangle(10, 20)
    assert rec.area() == 10 * 20

def test_area2(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle

def test_perimeter():
    rec = shapes.Rectangle(10, 20)
    assert rec.perimeter() == (10 * 2) + (20 * 2)