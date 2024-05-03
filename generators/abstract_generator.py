from abc import ABC, abstractmethod


class AbstractGenerator(ABC):

    @abstractmethod
    def create(self):
        ...
