from scipy.stats import norm

from generators.abstract_generator import AbstractGenerator
from uavs.uav import UAV
from worlds.coodrinate import Coordinate
from worlds.vector import Vector


class AircraftUAVGenerator(AbstractGenerator):

    def __init__(
        self,
        min_start_coordinate: Coordinate,
        max_start_coordinate: Coordinate,
        min_start_vector: Vector,
        max_start_vector: Vector,
        keep_start_vector: bool,
        num_of_steps: int
    ):
        self._min_start_coordinate = min_start_coordinate
        self._max_start_coordinate = max_start_coordinate
        self._min_start_vector = min_start_vector
        self._max_start_vector = max_start_vector
        self._keep_start_vector = keep_start_vector
        self._num_of_steps = num_of_steps

    def create(self, num_of_objects=1) -> list[UAV]:
        start_coordinates = [
            Coordinate(x, y, z)
            for x, y, z in zip(
                self.get_uniform_values(self._min_start_coordinate.y, self._max_start_coordinate.y, num_of_objects),
                self.get_uniform_values(self._min_start_coordinate.y, self._max_start_coordinate.y, num_of_objects),
                self.get_uniform_values(self._min_start_coordinate.z, self._max_start_coordinate.z, num_of_objects)
            )
        ]

        start_vectors = [
            Coordinate(x, y, z)
            for x, y, z in zip(
                self.get_uniform_values(self._min_start_vector.x, self._max_start_vector.x, num_of_objects),
                self.get_uniform_values(self._min_start_vector.y, self._max_start_vector.y, num_of_objects),
                self.get_uniform_values(self._min_start_vector.z, self._max_start_vector.z, num_of_objects)
            )
        ]

        return [
            UAV(self._create_route(start_coordinate, start_vector))
            for start_coordinate, start_vector in zip(start_coordinates, start_vectors)
        ]

    def _create_route(
        self,
        start_coordinate: Coordinate,
        start_vector: Coordinate
    ) -> list[Coordinate]:
        peek_alpha = Vector(start_vector.x, start_vector.y, 0).get_angle(Vector(1, 0, 0))
        peek_beta = Vector(start_vector.x, 0, start_vector.z).get_angle(Vector(1, 0, 0))

        route = [start_coordinate]
        coordinate = start_coordinate
        vector = start_vector
        for alpha, beta in zip(
            norm.rvs(loc=peek_alpha, scale=0.1, size=self._num_of_steps),
            norm.rvs(loc=peek_beta, scale=0.1, size=self._num_of_steps)
        ):
            x, y = Vector.get_vector(vector.x, vector.y, alpha)
            x, z = Vector.get_vector(x, vector.z, beta)
            coordinate += Coordinate(x, y, z)

            route.append(coordinate)

            if not self._keep_start_vector:
                vector = Coordinate(x, y, z)

        return route
