# Fixtures: provide re-usable test data to test-functions

from source.shapes import Rectangle
import pytest


@pytest.fixture()
def rectangle():
    return Rectangle(10, 20)


def test_area(rectangle):
    actual = rectangle.area()
    expected = rectangle.length * rectangle.width
    assert actual == expected


def test_perimeter(rectangle):
    actual = rectangle.perimeter()
    expected = 2 * (rectangle.length + rectangle.width)
    assert actual == expected
