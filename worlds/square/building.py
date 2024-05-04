import math

from matplotlib.patches import RegularPolygon

from worlds.abstract_world_object import AbstractWorldObject
from worlds.coodrinate import Coordinate


class SquareBuilding(AbstractWorldObject):

    def __init__(self, coordinate: Coordinate, height: int, side: int):
        self.coordinate = coordinate
        self.height = height
        self.side = side
        super().__init__()

    def create_patch(self) -> RegularPolygon:
        return RegularPolygon(
            xy=(self.coordinate.x, self.coordinate.y),
            numVertices=4,
            radius=math.sqrt(2 * self.side * self.side) / 2,
            orientation=0.25 * math.pi,
            edgecolor="brown",
            facecolor="white",
            hatch="xx",
        )
