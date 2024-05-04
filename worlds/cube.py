from worlds.coodrinate import Coordinate


class Cube:

    def __init__(self, coordinate: Coordinate, side: int):
        self.coordinate = coordinate
        self.side = side

    def __eq__(self, other):
        if not isinstance(other, Cube):
            return False

        return self.coordinate == other.coordinate and self.side == other.side
