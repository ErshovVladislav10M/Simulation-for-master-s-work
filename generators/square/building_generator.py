import numpy as np
from scipy.stats import norm

from generators.abstract_generator import AbstractGenerator
from worlds.coodrinate import Coordinate
from worlds.square.building import SquareBuilding


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
        max_side: int,
        num_of_buildings: int
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
        self._num_of_buildings = num_of_buildings

    def create(self) -> list[SquareBuilding]:
        possible_heights = np.arange(
            self._min_height,
            self._max_height,
            (self._max_height - self._min_height) / float(self._num_of_buildings)
        )
        possible_sides = np.arange(
            self._min_side,
            self._max_side,
            (self._max_side - self._min_side) / float(self._num_of_buildings)
        )

        height_distribution = [
            int(self._num_of_buildings * distribution)
            for distribution in norm.pdf(possible_heights, self._average_height, 5)
        ]
        side_distribution = [
            int(self._num_of_buildings * distribution)
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
            SquareBuilding(Coordinate(x=x, y=y), height, side)
            for x, y, height, side in zip(
                np.random.randint(self._min_x, self._max_x, self._num_of_buildings),
                np.random.randint(self._min_y, self._max_y, self._num_of_buildings),
                height_values,
                side_values
            )
        ]
