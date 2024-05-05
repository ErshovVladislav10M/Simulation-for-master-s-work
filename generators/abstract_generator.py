import math
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


class AbstractGenerator(ABC):

    @abstractmethod
    def create(self, num_of_objects=1) -> list:
        ...

    @staticmethod
    def get_norm_values(
        # min_value: float,
        # max_value: float,
        peak_value: float,
        num_of_values: int
    ) -> np.ndarray:
        # possible_values = np.arange(min_value, max_value, (max_value - min_value) / 1000.0)
        return norm.rvs(loc=peak_value, scale=1, size=num_of_values)


# values = AbstractGenerator.get_norm_values(math.pi, 10)
# plt.plot(range(len(values)), values)
# plt.show()