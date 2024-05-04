import math

from generators.abstract_generator import AbstractGenerator
from sensors.cube import Cube
from sensors.cube_area import CubeArea
from worlds.coodrinate import Coordinate


# TODO: create logic
class CameraCubeAreaGenerator(AbstractGenerator):

    def __init__(
        self,
        start_coordinate: Coordinate,
        finish_coordinate: Coordinate,
        cube_side: float
    ):
        self._start_coordinate = start_coordinate
        self._finish_coordinate = finish_coordinate
        self._distance = math.sqrt(
            math.pow(start_coordinate.x - finish_coordinate.x, 2)
            + math.pow(start_coordinate.y - finish_coordinate.y, 2)
        )
        self._cube_side = cube_side

    def create(self) -> list[CubeArea]:
        cubes = []
        for i in range(int(self._distance / self._cube_side)):
            cubes.extend(self._create_cubes(i))

        return [CubeArea(cubes)]

    def _create_cubes(self, num_of_level: int) -> list[Cube]:
        cubes = []
        for i in range(-num_of_level + 1, num_of_level - 1, 1):
            # for j in range(-num_of_level + 1, num_of_level - 1, 1):
            coordinate = Coordinate(
                x=self._start_coordinate.x + num_of_level * self._cube_side,
                y=self._start_coordinate.y + i * self._cube_side
            )
            cubes.append(Cube(coordinate, self._cube_side))

        return cubes
