import numpy as np
from scipy.stats import norm

from generators.abstract_generator import AbstractGenerator
from worlds.coodrinate import Coordinate
from worlds.city.building import SquareBuilding


class SquareBuildingGenerator(AbstractGenerator):

    def __init__(
        self,
        min_x: int,
        max_x: int,
        min_y: int,
        max_y: int,
        peak_height: int,
        scale_height: int,
        peak_side: int,
        scale_side: int
    ):
        self._min_x = min_x
        self._max_x = max_x
        self._min_y = min_y
        self._max_y = max_y
        self._peak_height = peak_height
        self._scale_height = scale_height
        self._peak_side = peak_side
        self._scale_side = scale_side

    def create(self, num_of_objects=1) -> list[SquareBuilding]:
        return [
            SquareBuilding(Coordinate(x=x, y=y, z=0), height, side)
            for x, y, height, side in zip(
                np.random.randint(self._min_x, self._max_x, num_of_objects),
                np.random.randint(self._min_y, self._max_y, num_of_objects),
                norm.rvs(loc=self._peak_height, scale=self._scale_height, size=num_of_objects),
                norm.rvs(loc=self._peak_side, scale=self._scale_side, size=num_of_objects)
            )
        ]
