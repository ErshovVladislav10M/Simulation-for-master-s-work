import numpy as np
from scipy.stats import norm

from generators.abstract_generator import AbstractGenerator
from sensors.cameras.camera import Camera
from worlds.coodrinate import Coordinate
from worlds.vector import Vector


class CameraGenerator(AbstractGenerator):

    def __init__(
        self,
        min_x: int,
        max_x: int,
        min_y: int,
        max_y: int,
        peek_height: int,
        scale_height: int,
        min_vector: Vector,
        max_vector: Vector,
        alpha: float,
        beta: float,
        initial_q: float,
        obsolescence_time: int
    ):
        self._min_x = min_x
        self._max_x = max_x
        self._min_y = min_y
        self._max_y = max_y
        self._peek_height = peek_height
        self._scale_height = scale_height
        self._min_vector = min_vector
        self._max_vector = max_vector
        self._alpha = alpha
        self._beta = beta
        self._initial_q = initial_q
        self._obsolescence_time = obsolescence_time

    def create(self, num_of_objects=1) -> list[Camera]:
        vectors = [
            Vector(x, y, z)
            for x, y, z in zip(
                self.get_uniform_values(self._min_vector.x, self._max_vector.x, num_of_objects),
                self.get_uniform_values(self._min_vector.y, self._max_vector.y, num_of_objects),
                self.get_uniform_values(self._min_vector.z, self._max_vector.z, num_of_objects)
            )
        ]

        return [
            Camera(
                id=id,
                coordinate=Coordinate(x, y, height),
                vector=vector,
                alpha=self._alpha,
                beta=self._beta,
                initial_q=self._initial_q,
                obsolescence_time=self._obsolescence_time
            )
            for id, x, y, height, vector in zip(
                range(num_of_objects),
                np.random.randint(self._min_x, self._max_x, num_of_objects),
                np.random.randint(self._min_y, self._max_y, num_of_objects),
                norm.rvs(loc=self._peek_height, scale=self._scale_height, size=num_of_objects),
                vectors
            )
        ]
