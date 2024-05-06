import numpy as np
from scipy.stats import norm

from generators.abstract_generator import AbstractGenerator
from generators.city.simple_camera_area_generator import SimpleCameraAreaGenerator
from sensors.cameras.camera import Camera
from worlds.coodrinate import Coordinate


class CameraGenerator(AbstractGenerator):

    def __init__(
        self,
        min_x: int,
        max_x: int,
        min_y: int,
        max_y: int,
        peek_height: int,
        scale_height: int,
        initial_q: float,
        obsolescence_time: int
    ):
        self._min_x = min_x
        self._max_x = max_x
        self._min_y = min_y
        self._max_y = max_y
        self._peek_height = peek_height
        self._scale_height = scale_height
        self._initial_q = initial_q
        self._obsolescence_time = obsolescence_time

    def create(self, num_of_objects=1) -> list[Camera]:
        return [
            Camera(
                id=id,
                area=SimpleCameraAreaGenerator(Coordinate(x, y, height), radius=5, cube_side=1).create()[0],
                coordinate=Coordinate(x, y, height),
                initial_q=self._initial_q,
                obsolescence_time=self._obsolescence_time
            )
            for id, x, y, height in zip(
                range(num_of_objects),
                np.random.randint(self._min_x, self._max_x, num_of_objects),
                np.random.randint(self._min_y, self._max_y, num_of_objects),
                norm.rvs(loc=self._peek_height, scale=self._scale_height, size=num_of_objects),
            )
        ]
