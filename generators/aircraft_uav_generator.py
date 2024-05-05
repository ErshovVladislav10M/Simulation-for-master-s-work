import math

from scipy.stats import norm

from generators.abstract_generator import AbstractGenerator
from uavs.uav import UAV
from worlds.coodrinate import Coordinate


class AircraftUAVGenerator(AbstractGenerator):

    def __init__(
        self,
        start_coordinate: Coordinate,
        start_vector: Coordinate,
        num_of_steps: int
    ):
        self._start_coordinate = start_coordinate
        self._start_vector = start_vector
        self._num_of_steps = num_of_steps

    def create(self, num_of_objects=1) -> list[UAV]:
        peek_alpha = self._get_angle(
            vector_1=Coordinate(self._start_vector.x, self._start_vector.y, 0),
            vector_2=Coordinate(1, 0, 0)
        )
        peek_beta = self._get_angle(
            vector_1=Coordinate(self._start_vector.x, 0, self._start_vector.z),
            vector_2=Coordinate(1, 0, 0)
        )

        route = [self._start_coordinate]
        coordinate = self._start_coordinate
        vector = self._start_vector
        for alpha, beta in zip(
            norm.rvs(loc=peek_alpha, scale=0.1, size=self._num_of_steps),
            norm.rvs(loc=peek_beta, scale=0.1, size=self._num_of_steps)
        ):
            x, y = self._get_vector(vector.x, vector.y, alpha)
            x, z = self._get_vector(x, vector.z, beta)
            vector = Coordinate(x, y, z)
            coordinate += vector

            route.append(coordinate)

        return [UAV(route)]

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
