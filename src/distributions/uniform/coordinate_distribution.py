import numpy as np

from src.distributions.abstract_distribution import AbstractDistribution
from src.worlds.coodrinate import Coordinate


class UniformCoordinateDistribution(AbstractDistribution):

    def __init__(self, min_value: Coordinate, max_value: Coordinate):
        self._min_value = min_value
        self._max_value = max_value

    def get_values(self, num_of_values: int) -> list[Coordinate]:
        x = self._max_value.x - self._min_value.x
        x_values = [x * np.random.random() + self._min_value.x for _ in range(num_of_values)]
        y = self._max_value.y - self._min_value.y
        y_values = [y * np.random.random() + self._min_value.y for _ in range(num_of_values)]
        z = self._max_value.z - self._min_value.z
        z_values = [z * np.random.random() + self._min_value.z for _ in range(num_of_values)]

        return [
            Coordinate(x, y, z)
            for x, y, z in zip(x_values, y_values, z_values)
        ]
