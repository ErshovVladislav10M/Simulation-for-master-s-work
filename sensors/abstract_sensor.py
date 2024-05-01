from abc import ABC

from worlds.area import Area


class AbstractSensor(ABC):

    def __init__(self, world: World, area: Area):
        self._world = world
        self._area = area
        self._measurements = []
        self._initial_q = initial_q