from sensors.cube import Cube
from worlds.coodrinate import Coordinate


class CubeArea:

    def __init__(self, cubes: list[Cube]):
        self.cubes = cubes

    def contain(self, coordinate: Coordinate) -> bool:
        for cube in self.cubes:
            if cube.contain(coordinate):
                return True

        return False
