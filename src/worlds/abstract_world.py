import threading
from abc import ABC, abstractmethod

from src.uavs.uav import UAV


class AbstractWorld(ABC, threading.Thread):

    def __init__(self, simulation_data: dict):
        super().__init__()
        self.actual_step = 0
        self._num_of_steps = simulation_data["num_of_steps"]
        self.size = simulation_data["world_size"]
        self._create_step_images = simulation_data["create_step_images"]

    @abstractmethod
    def rec_messages(self) -> None:
        pass

    @abstractmethod
    def send_messages(self) -> None:
        pass

    @abstractmethod
    def do_step(self) -> None:
        pass

    @abstractmethod
    def get_uavs(self) -> list[UAV]:
        pass
