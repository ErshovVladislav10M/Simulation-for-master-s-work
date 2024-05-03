from abc import ABC

from worlds.area import Area
from worlds.square.world import SquareWorld


class AbstractSensor(ABC):

    def __init__(self, world: SquareWorld, area: Area):
        self._world = world
        self._area = area
        self._measurements = []
