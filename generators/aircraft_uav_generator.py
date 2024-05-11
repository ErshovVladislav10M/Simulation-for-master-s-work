from scipy.stats import norm

from distributions.abstract_distribution import AbstractDistribution
from generators.abstract_generator import AbstractGenerator
from uavs.uav import UAV
from worlds.coodrinate import Coordinate
from worlds.vector import Vector


class AircraftUAVGenerator(AbstractGenerator):

    def __init__(
        self,
        start_coordinate_distribution: AbstractDistribution,
        start_vector_distribution: AbstractDistribution,
        keep_start_vector: bool,
        num_of_steps: int
    ):
        self._start_coordinate_distribution = start_coordinate_distribution
        self._start_vector_distribution = start_vector_distribution
        self._keep_start_vector = keep_start_vector
        self._num_of_steps = num_of_steps

    def create(self, num_of_objects=1) -> list[UAV]:
        return [
            UAV(self._create_route(start_coordinate, start_vector))
            for start_coordinate, start_vector in zip(
                self._start_coordinate_distribution.get_values(num_of_objects),
                self._start_vector_distribution.get_values(num_of_objects)
            )
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
