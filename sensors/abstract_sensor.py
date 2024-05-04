from abc import ABC

from sensors.cube_area import CubeArea
from worlds.square.world import SquareWorld


class AbstractSensor(ABC):

    def __init__(self, world: SquareWorld, area: CubeArea):
        self._world = world
        self._area = area
        self._measurements = []
