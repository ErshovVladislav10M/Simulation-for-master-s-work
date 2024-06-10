from src.distributions.abstract_distribution import AbstractDistribution
from src.distributions.distribution_utils import get_distribution
from src.generators.abstract_generator import AbstractGenerator
from src.sensors.cameras.camera import Camera


class CameraGenerator(AbstractGenerator):

    def __init__(
        self,
        coordinate_distribution: AbstractDistribution,
        sensor_data: dict,
        distance_distribution: AbstractDistribution,
        cube_side: float,
        obsolescence_time: int
    ):
        self._coordinate_distribution = coordinate_distribution
        self._height_distribution = get_distribution(sensor_data["height_distribution"])
        self._sensor_data = sensor_data
        self._direction_vector_distribution = get_distribution(sensor_data["direction_vector_distribution"])
        self._distance_distribution = distance_distribution
        self._cube_side = cube_side
        self._obsolescence_time = obsolescence_time

    def create(self, num_of_objects=1) -> list[Camera]:
        return [
            Camera(
                identifier=identifier,
                coordinate=coordinate,
                direction_vector=direction_vector,
                distance=distance,
                sensor_data=self._sensor_data,
                cube_side=self._cube_side,
                obsolescence_time=self._obsolescence_time
            )
            for identifier, coordinate, height, direction_vector, distance in zip(
                range(num_of_objects),
                self._coordinate_distribution.get_values(num_of_objects),
                self._height_distribution.get_values(num_of_objects),
                self._direction_vector_distribution.get_values(num_of_objects),
                self._distance_distribution.get_values(num_of_objects)
            )
        ]
