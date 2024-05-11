import threading
from abc import ABC, abstractmethod

from uavs.uav import UAV


class AbstractWorld(ABC, threading.Thread):

    def __init__(self, num_steps: int, world_size: float, create_step_images: bool):
        super().__init__()
        self.actual_step = 0
        self._num_steps = num_steps
        self.size = world_size
        self._create_step_images = create_step_images

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
