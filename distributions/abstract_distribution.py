from abc import ABC, abstractmethod


class AbstractDistribution(ABC):

    @abstractmethod
    def get_values(self, num_of_values: int) -> list:
        ...
