from generators.abstract_generator import AbstractGenerator
from sensors.cube import Cube
from sensors.cube_area import CubeArea
from worlds.coodrinate import Coordinate


class SimpleCameraAreaGenerator(AbstractGenerator):

    def __init__(
        self,
        start_coordinate: Coordinate,
        radius: float,
        cube_side: float
    ):
        self._start_coordinate = start_coordinate
        self._radius = radius
        self._cube_side = cube_side

    def create(self, num_of_objects=1) -> list[CubeArea]:
        cubes = []
        for i in range(
            int((self._start_coordinate.x - self._radius) / self._cube_side),
            int((self._start_coordinate.x + self._radius) / self._cube_side),
            1
        ):
            for j in range(
                int((self._start_coordinate.y - self._radius) / self._cube_side),
                int((self._start_coordinate.y + self._radius) / self._cube_side),
                1
            ):
                coordinate = Coordinate(x=i * self._cube_side, y=j * self._cube_side)
                cubes.append(Cube(coordinate, self._cube_side))

        return [CubeArea(cubes)]
