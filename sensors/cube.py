import math

import numpy as np
from matplotlib.patches import RegularPolygon

from worlds.abstract_world_object import AbstractWorldObject
from worlds.coodrinate import Coordinate


class Cube(AbstractWorldObject):

    def __init__(self, coordinate: Coordinate, side: float, q: float):
        self.coordinate = coordinate
        self.side = side
        self.diagonal = side * math.sqrt(2)
        self.q = q
        super().__init__()

    def create_xy_patch(self) -> RegularPolygon:
        return RegularPolygon(
            xy=(self.coordinate.x, self.coordinate.y),
            numVertices=4,
            orientation=0.25 * math.pi,
            radius=self.diagonal / 2,
            edgecolor="red",
            alpha=self.q,
            facecolor="white",
        )

    def contain(self, coordinate: Coordinate, radius: float = 0) -> bool:
        if coordinate is None:
            return False

        # if self.coordinate.z + 0.5 * self.side < coordinate.z:
        #     return False
        # if self.coordinate.z - 0.5 * self.side > coordinate.z:
        #     return False

        return super().contain(coordinate, radius)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Cube):
            return False

        return self.coordinate == other.coordinate\
            and np.isclose(self.side, other.side)\
            and np.isclose(self.q, other.q)

    def __str__(self):
        return "coordinate = " + str(self.coordinate)\
            + ", side = " + str(self.side)\
            + ", q = " + str(self.q)
