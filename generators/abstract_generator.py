from abc import ABC, abstractmethod

import numpy as np


class AbstractGenerator(ABC):

    @abstractmethod
    def create(self, num_of_objects=1) -> list:
        ...

    @staticmethod
    def get_uniform_values(min_value: float, max_value: float, num_of_values) -> list[float]:
        return [
            (max_value - min_value) * np.random.random() + min_value
            for _ in range(num_of_values)
        ]

    # @staticmethod
    # def get_norm_values(
    #     min_value: float,
    #     max_value: float,
    #     peak_value: float,
    #     scale: float,
    #     num_of_values: int
    # ):# -> np.ndarray:
    #     possible_values = np.arange(min_value, max_value, (max_value - min_value) / 1000.0)
    #     distribution = norm.pdf(possible_values, loc=peak_value, scale=scale)
    #     some_distribution = rv_discrete(
    #         name='some_distribution',
    #         values=(possible_values, distribution)
    #     )
    #     # plt.plot(possible_values, distribution)
    #     # plt.show()
    #     return norm.rvs(size=num_of_values)

# values = AbstractGenerator.get_norm_values(2, 10, 5, 1, 10)
# plt.plot(range(len(values)), values)
# plt.show()
