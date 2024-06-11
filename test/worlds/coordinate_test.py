import math

import pytest

from src.worlds.coodrinate import Coordinate


def test_init():
    coordinate = Coordinate(0, 0, 0)

    assert coordinate.x == 0
    assert coordinate.y == 0
    assert coordinate.z == 0


def test_of():
    coordinate1 = Coordinate(0, 0, 0)
    coordinate2 = Coordinate(0, 0, 0)

    assert coordinate1 == coordinate2


def test_distance():
    coordinate1 = Coordinate(1, 0, 0)
    coordinate2 = Coordinate(0, 0, 0)

    assert coordinate1.distance(coordinate2) == 1


def test_eq():
    assert Coordinate(0, 0, 0) != "str"


def test_add_coordinate():
    coordinate1 = Coordinate(1, 1, 1)
    coordinate2 = Coordinate(1, 1, 1)

    assert coordinate1 + coordinate2 == Coordinate(2, 2, 2)


def test_add_float():
    coordinate1 = Coordinate(1, 1, 1)
    other = 1.0

    assert coordinate1 + other == Coordinate(2, 2, 2)


def test_add_int():
    coordinate1 = Coordinate(1, 1, 1)
    other = 1

    assert coordinate1 + other == Coordinate(2, 2, 2)


def test_add_error():
    coordinate1 = Coordinate(1, 1, 1)
    other = "str"

    with pytest.raises(ValueError):
        coordinate1 + other


def test_sub_coordinate():
    coordinate1 = Coordinate(1, 1, 1)
    coordinate2 = Coordinate(1, 1, 1)

    assert coordinate1 - coordinate2 == Coordinate(0, 0, 0)


def test_sub_float():
    coordinate1 = Coordinate(1, 1, 1)
    other = 1.0

    assert coordinate1 - other == Coordinate(0, 0, 0)


def test_sub_int():
    coordinate1 = Coordinate(1, 1, 1)
    other = 1

    assert coordinate1 - other == Coordinate(0, 0, 0)


def test_sub_error():
    coordinate1 = Coordinate(1, 1, 1)
    other = "str"

    with pytest.raises(ValueError):
        coordinate1 - other


def test_mul_coordinate():
    coordinate1 = Coordinate(1, 2, 3)
    coordinate2 = Coordinate(1, 2, 3)

    assert math.isclose(coordinate1 * coordinate2, 14)


def test_mul_float():
    coordinate1 = Coordinate(1, 1, 1)
    other = 1.0

    assert coordinate1 * other == Coordinate(1, 1, 1)


def test_mul_int():
    coordinate1 = Coordinate(1, 1, 1)
    other = 1

    assert coordinate1 * other == Coordinate(1, 1, 1)


def test_mul_error():
    coordinate = Coordinate(1, 1, 1)
    other = "str"

    with pytest.raises(ValueError):
        coordinate * other


def test_str():
    coordinate = Coordinate(1, 1, 1)

    assert str(coordinate) == "[1, 1, 1]"
