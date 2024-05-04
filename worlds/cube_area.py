from worlds.cube import Cube
from uavs.uav import UAV


class CubeArea:

    def __init__(self, cubes: list[Cube]):
        self._cubes = cubes

    def contain(self, uav: UAV) -> bool:
        return self._cubes.count(uav.get_position()) > 0

    @property
    def cubes(self):
        return self._cubes
