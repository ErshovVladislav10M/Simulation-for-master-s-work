from abc import ABC

from worlds.area import Area
from worlds.world import World


class AbstractSensor(ABC):

    def __init__(self, world: World, area: Area):
        self._world = world
        self._area = area
        self._measurements = []
