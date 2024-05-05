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
        average_height: int,
        min_height: int,
        max_height: int,
        average_side: int,
        min_side: int,
        max_side: int
    ):
        self._min_x = min_x
        self._max_x = max_x
        self._min_y = min_y
        self._max_y = max_y
        self._average_height = average_height
        self._min_height = min_height
        self._max_height = max_height
        self._average_side = average_side
        self._min_side = min_side
        self._max_side = max_side

    def create(self, num_of_objects=1) -> list[SquareBuilding]:
        possible_heights = np.arange(
            self._min_height,
            self._max_height,
            (self._max_height - self._min_height) / 1000.0
        )
        possible_sides = np.arange(
            self._min_side,
            self._max_side,
            (self._max_side - self._min_side) / 1000.0
        )

        height_distribution = [
            int(1000 * distribution)
            for distribution in norm.pdf(possible_heights, self._average_height, 5)
        ]
        side_distribution = [
            int(1000 * distribution)
            for distribution in norm.pdf(possible_sides, self._average_side, 5)
        ]

        height_values = []
        for side, distribution in zip(possible_heights, height_distribution):
            for _ in range(distribution):
                height_values.append(side)

        side_values = []
        for side, distribution in zip(possible_sides, side_distribution):
            for _ in range(distribution):
                side_values.append(side)

        return [
            SquareBuilding(Coordinate(x=x, y=y, z=height), height, side)
            for x, y, height, side in zip(
                np.random.randint(self._min_x, self._max_x, num_of_objects),
                np.random.randint(self._min_y, self._max_y, num_of_objects),
                height_values,
                side_values
            )
        ]
