from abc import abstractmethod

from src.measurements.measurement import Measurement
from src.worlds.abstract_world import AbstractWorld
from src.worlds.abstract_world_object import AbstractWorldObject


class AbstractSensor(AbstractWorldObject):

    def __init__(self, id: int):
        self.id = id
        self._measurements: list[Measurement] = []
        super().__init__()

    @abstractmethod
    def rec_measurements(self, world: AbstractWorld, measurements: list[Measurement]) -> None:
        ...

    @abstractmethod
    def send_measurements(self, world: AbstractWorld) -> list[Measurement]:
        ...

    @abstractmethod
    def do_measurement(self, world: AbstractWorld):
        ...

    @abstractmethod
    def get_all_measurements(self) -> list[Measurement]:
        ...

    @abstractmethod
    def get_actual_measurements(self, actual_step: int) -> list[Measurement]:
        ...
