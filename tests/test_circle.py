# Class based tests: group your tests in a class

from source.shapes import Circle
from math import pi


class TestCircle:
    def setup_method(self, method):
        self.circle = Circle(10)

    def teardown_method(self, method):
        del self.circle

    def test_area(self):
        actual = self.circle.area()
        expected = self.circle.radius ** 2 * pi
        assert actual == expected

    def test_perimeter(self):
        actual = self.circle.perimeter()
        expected = 2 * self.circle.radius * pi
        assert actual == expected
