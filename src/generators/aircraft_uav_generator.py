from scipy.stats import norm

from src.distributions.abstract_distribution import AbstractDistribution
from src.generators.abstract_generator import AbstractGenerator
from src.uavs.uav import UAV
from src.worlds.coodrinate import Coordinate
from src.worlds.vector import Vector


class AircraftUAVGenerator(AbstractGenerator):

    def __init__(
        self,
        start_coordinate_distribution: AbstractDistribution,
        start_direction_vector_distribution: AbstractDistribution,
        speed_distribution: AbstractDistribution,
        keep_start_vector: bool,
        num_of_steps: int,
        world_size: float
    ):
        self._start_coordinate_distribution = start_coordinate_distribution
        self._start_direction_vector_distribution = start_direction_vector_distribution
        self._speed_distribution = speed_distribution
        self._keep_start_vector = keep_start_vector
        self._num_of_steps = num_of_steps
        self._world_size = world_size

    def create(self, num_of_objects=1) -> list[UAV]:
        return [
            UAV(self._create_route(start_coordinate, start_direction_vector, speed))
            for start_coordinate, start_direction_vector, speed in zip(
                self._start_coordinate_distribution.get_values(num_of_objects),
                self._start_direction_vector_distribution.get_values(num_of_objects),
                self._speed_distribution.get_values(num_of_objects)
            )
        ]

    def _create_route(
        self,
        start_coordinate: Coordinate,
        start_direction_vector: Vector,
        speed: float
    ) -> list[Coordinate]:
        peek_alpha = Vector(start_direction_vector.x, start_direction_vector.y, 0).get_angle(Vector(1, 0, 0))
        peek_beta = Vector(start_direction_vector.x, 0, start_direction_vector.z).get_angle(Vector(1, 0, 0))

        route = [start_coordinate]
        coordinate = start_coordinate
        vector = start_direction_vector
        for alpha, beta in zip(
            norm.rvs(loc=peek_alpha, scale=0.1, size=self._num_of_steps),
            norm.rvs(loc=peek_beta, scale=0.1, size=self._num_of_steps)
        ):
            new_vector = vector.rotate(alpha=alpha, beta=0)
            coordinate += new_vector / new_vector.length() * speed

            if coordinate.x > self._world_size:
                coordinate.x -= 2 * self._world_size
            if coordinate.x < -self._world_size:
                coordinate.x += 2 * self._world_size
            if coordinate.y > self._world_size:
                coordinate.y -= 2 * self._world_size
            if coordinate.y < -self._world_size:
                coordinate.y += 2 * self._world_size

            route.append(coordinate)

            if not self._keep_start_vector:
                vector = new_vector

        return route