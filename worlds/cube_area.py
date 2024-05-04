from worlds.cube import Cube
from uavs.uav import UAV


class CubeArea:

    def __init__(self, cubes: list[Cube]):
        self.cubes = cubes

    def contain(self, uav: UAV) -> bool:
        return self.cubes.count(uav.get_position()) > 0
