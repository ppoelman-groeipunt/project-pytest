# Parametrize: try same test with different values

from source.shapes import Square
import pytest

data = [(0, 0), (5, 25), (10, 100)]


@pytest.mark.parametrize('x, expected', data)
def test_area(x, expected):
    actual = Square(x).area()
    assert actual == expected


@pytest.mark.parametrize('x, expected', [(0, 0), (5, 20), (10, 40)])
def test_perimeter(x, expected):
    actual = Square(x).perimeter()
    assert actual == expected
