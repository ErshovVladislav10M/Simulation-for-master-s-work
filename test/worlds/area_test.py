from src.worlds.area import Area
from src.worlds.coodrinate import Coordinate


def test():
    coordinates = [
        Coordinate(0, 0, 0),
        Coordinate(1, 0, 0),
        Coordinate(1, 1, 0),
        Coordinate(0, 1, 0),
    ]

    area = Area(coordinates=coordinates)

    assert area._yz_patch is None
    assert area._xz_patch is None

    assert area.contain(coordinate=Coordinate(0.5, 0.5, 0))
