from worlds.coodrinate import Coordinate


class SquareBuilding:

    def __init__(self, coordinate: Coordinate, height: int, side: int):
        self.coordinate = coordinate
        self.height = height
        self.side = side