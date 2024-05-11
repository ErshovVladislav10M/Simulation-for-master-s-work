import numpy as np

from distributions.abstract_distribution import AbstractDistribution
from worlds.vector import Vector


class UniformVectorDistribution(AbstractDistribution):

    def __init__(self, min_value: Vector, max_value: Vector):
        self._min_value = min_value
        self._max_value = max_value

    def get_values(self, num_of_values: int) -> list[Vector]:
        x_values = [
            (self._max_value.x - self._min_value.x) * np.random.random() + self._min_value.x
            for _ in range(num_of_values)
        ]
        y_values = [
            (self._max_value.y - self._min_value.y) * np.random.random() + self._min_value.y
            for _ in range(num_of_values)
        ]
        z_values = [
            (self._max_value.z - self._min_value.z) * np.random.random() + self._min_value.z
            for _ in range(num_of_values)
        ]

        return [
            Vector(x, y, z)
            for x, y, z in zip(x_values, y_values, z_values)
        ]
