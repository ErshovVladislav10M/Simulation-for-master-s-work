from abc import ABC, abstractmethod


class AbstractGenerator(ABC):

    @abstractmethod
    def create(self, num_of_objects=1) -> list:
        ...
