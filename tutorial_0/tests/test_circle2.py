import pytest
import math
import source.shapes as shapes

class TestCircle:
    def setup_method(self, method):
        print(f"setting up {method}")
        self.circle = shapes.Circle(10)

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()
