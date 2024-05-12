from distributions.abstract_distribution import AbstractDistribution
from generators.abstract_generator import AbstractGenerator
from sensors.cameras.camera import Camera


class CameraGenerator(AbstractGenerator):

    def __init__(
        self,
        coordinate_distribution: AbstractDistribution,
        height_distribution: AbstractDistribution,
        alpha: float,
        beta: float,
        vector_distribution: AbstractDistribution,
        distance_distribution: AbstractDistribution,
        cube_side: float,
        initial_q: float,
        obsolescence_time: int
    ):
        self._coordinate_distribution = coordinate_distribution
        self._height_distribution = height_distribution
        self._alpha = alpha
        self._beta = beta
        self._vector_distribution = vector_distribution
        self._distance_distribution = distance_distribution
        self._cube_side = cube_side
        self._initial_q = initial_q
        self._obsolescence_time = obsolescence_time

    def create(self, num_of_objects=1) -> list[Camera]:
        return [
            Camera(
                id=id,
                coordinate=coordinate,
                vector=vector,
                distance=distance,
                alpha=self._alpha,
                beta=self._beta,
                cube_side=self._cube_side,
                initial_q=self._initial_q,
                obsolescence_time=self._obsolescence_time
            )
            for id, coordinate, height, vector, distance in zip(
                range(num_of_objects),
                self._coordinate_distribution.get_values(num_of_objects),
                self._height_distribution.get_values(num_of_objects),
                self._vector_distribution.get_values(num_of_objects),
                self._distance_distribution.get_values(num_of_objects)
            )
        ]
