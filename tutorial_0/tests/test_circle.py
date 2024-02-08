import pytest
import math
import source.shapes as shapes

class TestCircle:
    def setup_method(self, method):
        print(f"setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"tearing down {method}")
        

    def test_one(self):
        assert True

    def test_two(self):
        assert True
    
    def test_radius(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected