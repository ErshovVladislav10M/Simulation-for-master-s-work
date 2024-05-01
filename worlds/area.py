from measurements.cube import Cube
from uavs.uav import UAV


class Area:

    def __init__(self, cubes: list[Cube]):
        self._cubes = cubes

    def contain(self, uav: UAV) -> bool:
        return self._cubes.count(uav.get_position()) > 0
