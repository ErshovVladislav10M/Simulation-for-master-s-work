import numpy as np
from scipy.stats import norm

from generators.abstract_generator import AbstractGenerator
from sensors.camera import Camera
from worlds.abstract_world import AbstractWorld
from worlds.coodrinate import Coordinate


class CameraGenerator(AbstractGenerator):

    def __init__(
        self,
        world: AbstractWorld,
        min_x: int,
        max_x: int,
        min_y: int,
        max_y: int,
        average_height: int,
        min_height: int,
        max_height: int,
        initial_q: float,
        obsolescence_time: int,
        num_of_cameras: int
    ):
        self._world = world
        self._min_x = min_x
        self._max_x = max_x
        self._min_y = min_y
        self._max_y = max_y
        self._average_height = average_height
        self._min_height = min_height
        self._max_height = max_height
        self._initial_q = initial_q
        self._obsolescence_time = obsolescence_time
        self._num_of_buildings = num_of_cameras

    def create(self) -> list[Camera]:
        possible_heights = np.arange(
            self._min_height,
            self._max_height,
            (self._max_height - self._min_height) / float(self._num_of_buildings)
        )
        height_distribution = [
            int(self._num_of_buildings * distribution)
            for distribution in norm.pdf(possible_heights, self._average_height, 5)
        ]

        height_values = []
        for side, distribution in zip(possible_heights, height_distribution):
            for _ in range(distribution):
                height_values.append(side)

        return [
            Camera(
                id=id,
                world=self._world,
                area=None,
                coordinate=Coordinate(x, y, height),
                height=height,
                initial_q=self._initial_q,
                obsolescence_time=self._obsolescence_time
            )
            for id, x, y, height in zip(
                range(len(height_values)),
                np.random.randint(self._min_x, self._max_x, self._num_of_buildings),
                np.random.randint(self._min_y, self._max_y, self._num_of_buildings),
                height_values
            )
        ]
