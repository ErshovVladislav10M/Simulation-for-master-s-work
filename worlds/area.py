import matplotlib
import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path

from worlds.abstract_world_object import AbstractWorldObject
from worlds.coodrinate import Coordinate


class Area(AbstractWorldObject):

    def __init__(self, coordinates: list[Coordinate]):
        self.coordinates = coordinates
        super().__init__()

    def create_xy_patch(self) -> PathPatch:
        vertices = np.array(
            [
                (coordinate.x, coordinate.y)
                for coordinate in self.coordinates
            ]
        )
        path = Path(vertices=vertices)

        return matplotlib.patches.PathPatch(
            path,
            fill=False,
            hatch="o"
        )
