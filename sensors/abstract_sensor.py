from abc import abstractmethod

from measurements.measurement import Measurement
from worlds.abstract_world import AbstractWorld
from worlds.abstract_world_object import AbstractWorldObject


class AbstractSensor(AbstractWorldObject):

    def __init__(self, id: int):
        self.id = id
        self._measurements = []
        super().__init__()

    @abstractmethod
    def do_measurement(self, world: AbstractWorld):
        ...

    @abstractmethod
    def get_all_measurements(self) -> list[Measurement]:
        ...

    @abstractmethod
    def get_actual_measurements(self, actual_step: int) -> list[Measurement]:
        ...
