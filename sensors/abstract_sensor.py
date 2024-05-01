from abc import ABC, abstractmethod

from measurements.measurement import Measurement
from words.area import Area


class AbstractSensor(ABC):

    def __init__(self, area: Area):
        self.area = area

    @abstractmethod
    def get_measurement(self) -> list[Measurement]:
        pass
