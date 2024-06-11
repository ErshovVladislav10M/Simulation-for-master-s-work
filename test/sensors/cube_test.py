from src.sensors.cube import Cube
from src.worlds.coodrinate import Coordinate


def test():
    coordinate = Coordinate(0, 0, 0)
    side = 1
    q = 0.5
    cube = Cube(coordinate=coordinate, side=side, q=q)

    assert cube.coordinate == coordinate
    assert cube.side == side
    assert cube.q == q
