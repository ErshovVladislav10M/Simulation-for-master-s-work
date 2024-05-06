import math

from scipy.stats import norm

from generators.abstract_generator import AbstractGenerator
from uavs.uav import UAV
from worlds.coodrinate import Coordinate


class AircraftUAVGenerator(AbstractGenerator):

    def __init__(
        self,
        min_start_coordinate: Coordinate,
        max_start_coordinate: Coordinate,
        min_start_vector: Coordinate,
        max_start_vector: Coordinate,
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
        peek_alpha = self._get_angle(
            vector_1=Coordinate(start_vector.x, start_vector.y, 0),
            vector_2=Coordinate(1, 0, 0)
        )
        peek_beta = self._get_angle(
            vector_1=Coordinate(start_vector.x, 0, start_vector.z),
            vector_2=Coordinate(1, 0, 0)
        )

        route = [start_coordinate]
        coordinate = start_coordinate
        vector = start_vector
        for alpha, beta in zip(
            norm.rvs(loc=peek_alpha, scale=0.1, size=self._num_of_steps),
            norm.rvs(loc=peek_beta, scale=0.1, size=self._num_of_steps)
        ):
            x, y = self._get_vector(vector.x, vector.y, alpha)
            x, z = self._get_vector(x, vector.z, beta)
            coordinate += Coordinate(x, y, z)

            route.append(coordinate)

            if not self._keep_start_vector:
                vector = Coordinate(x, y, z)

        return route

    @staticmethod
    def _get_angle(vector_1: Coordinate, vector_2: Coordinate) -> float:
        vector_1_length = math.sqrt(
            math.pow(vector_1.x, 2)
            + math.pow(vector_1.y, 2)
            + math.pow(vector_1.z, 2)
        )
        vector_2_length = math.sqrt(
            math.pow(vector_2.x, 2)
            + math.pow(vector_2.y, 2)
            + math.pow(vector_2.z, 2)
        )

        return math.asin(
            vector_1 * vector_2 / vector_1_length / vector_2_length
        )

    @staticmethod
    def _get_vector(first: float, second: float, angle: float) -> tuple[float, float]:
        return (
            first * math.cos(angle) - second * math.sin(angle),
            second * math.cos(angle) + first * math.sin(angle)
        )
