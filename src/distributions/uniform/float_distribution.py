import numpy as np

from src.distributions.abstract_distribution import AbstractDistribution


class UniformFloatDistribution(AbstractDistribution):

    def __init__(self, min_value: float, max_value: float):
        self._min_value = min_value
        self._max_value = max_value

    def get_values(self, num_of_values: int) -> list[float]:
        return [
            (self._max_value - self._min_value) * np.random.random() + self._min_value
            for _ in range(num_of_values)
        ]
