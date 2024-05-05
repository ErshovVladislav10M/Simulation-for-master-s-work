import numpy as np

from worlds.coodrinate import Coordinate


class Cube:

    def __init__(self, coordinate: Coordinate, side: float):
        self.coordinate = coordinate
        self.side = side

    def contain(self, coordinate: Coordinate) -> bool:
        if coordinate is None:
            return False

        if self.coordinate.x + 0.5 * self.side < coordinate.x:
            return False
        if self.coordinate.x - 0.5 * self.side > coordinate.x:
            return False
        if self.coordinate.y + 0.5 * self.side < coordinate.y:
            return False
        if self.coordinate.y - 0.5 * self.side > coordinate.y:
            return False
        if self.coordinate.z + 0.5 * self.side < coordinate.z:
            return False
        if self.coordinate.z - 0.5 * self.side > coordinate.z:
            return False

        return True

    def __eq__(self, other) -> bool:
        if not isinstance(other, Cube):
            return False

        return self.coordinate == other.coordinate\
            and np.isclose(self.side, other.side)
