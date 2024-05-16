# Function based tests

from source.my_functions import *
import pytest


def test_add():
    assert add(1, 4) == 5
    assert add(-2, 3) == 1


def test_divide():
    assert divide(10, 5) == 2


def test_add_float():
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert divide(10, 0)
