import math

import matplotlib
import numpy as np
from matplotlib.patches import RegularPolygon, PathPatch
from matplotlib.path import Path

from measurements.measurement import Measurement
from sensors.abstract_sensor import AbstractSensor
from sensors.cube import Cube
from worlds.abstract_world import AbstractWorld
from worlds.coodrinate import Coordinate
from worlds.vector import Vector


class Camera(AbstractSensor):

    def __init__(
        self,
        id: int,
        coordinate: Coordinate,
        vector: Vector,
        distance: float,
        alpha: float,
        beta: float,
        cube_side: float,
        initial_q: float,
        obsolescence_time: int
    ):
        self._coordinate = coordinate

        left_vector = vector.rotate(alpha=0.5 * alpha, beta=0)
        self._left_coordinate = coordinate + left_vector / left_vector.length() * distance
        right_vector = vector.rotate(alpha=-0.5 * alpha, beta=0)
        self._right_coordinate = coordinate + right_vector / right_vector.length() * distance
        up_vector = vector.rotate(alpha=0, beta=0.5 * beta)
        self._up_coordinate = coordinate + up_vector / up_vector.length() * distance
        down_vector = vector.rotate(alpha=0, beta=-0.5 * beta)
        self._down_coordinate = coordinate + down_vector / down_vector.length() * distance

        self._cube_side = cube_side
        self._cube_diagonal = cube_side * math.sqrt(2)
        self._initial_q = initial_q
        self._obsolescence_time = obsolescence_time
        super().__init__(id)

    def create_xy_patch(self) -> PathPatch:
        vertices = np.array(
            [
                (self._left_coordinate.x, self._left_coordinate.y),
                (self._coordinate.x, self._coordinate.y),
                (self._right_coordinate.x, self._right_coordinate.y)
            ]
        )
        path = Path(vertices=vertices)

        return matplotlib.patches.PathPatch(
            path,
            fill=False,
            edgecolor="blue",
            alpha=0.2
        )

    def create_xz_patch(self) -> PathPatch:
        vertices = np.array(
            [
                (self._up_coordinate.x, self._up_coordinate.z),
                (self._coordinate.x, self._coordinate.z),
                (self._down_coordinate.x, self._down_coordinate.z)
            ]
        )

        return matplotlib.patches.PathPatch(Path(vertices=vertices))

    def create_yz_patch(self) -> PathPatch:
        vertices = np.array(
            [
                (self._up_coordinate.y, self._up_coordinate.z),
                (self._coordinate.y, self._coordinate.z),
                (self._down_coordinate.y, self._down_coordinate.z)
            ]
        )

        return matplotlib.patches.PathPatch(Path(vertices=vertices))

    def rec_measurements(self, world: AbstractWorld, measurements: list[Measurement]) -> None:
        for measurement in measurements:
            for self_measurement in self.get_actual_measurements(world.actual_step):
                self_measurement.compare_and_update(measurement)

    def send_measurements(self, world: AbstractWorld) -> list[Measurement]:
        return self.get_actual_measurements(world.actual_step)

    def do_measurement(self, world: AbstractWorld) -> None:
        uavs_in_area = [
            uav
            for uav in world.get_uavs()
            if self.contain(uav.get_coordinate())
        ]

        for uav in uavs_in_area:
            measurement = Measurement(self.id, self._get_cubes(uav.get_coordinate()), world.actual_step)
            self._measurements.append(measurement)

    def _get_cubes(self, coordinate: Coordinate) -> list[(Cube, float)]:
        vector = Vector.of(coordinate - self._coordinate)
        vector_delta = (vector / vector.length()) * self._cube_diagonal

        coordinate = Coordinate(self._coordinate.x, self._coordinate.y, self._coordinate.z)
        cubes = []
        for _ in range(int(vector.length() / self._cube_diagonal)):
            cubes.append(Cube(coordinate, self._cube_side, self._initial_q))
            coordinate += vector_delta

        return cubes

    def get_all_measurements(self) -> list[Measurement]:
        return self._measurements

    def get_actual_measurements(self, actual_step: int) -> list[Measurement]:
        return [
            measurement
            for measurement in self._measurements
            if abs(actual_step - measurement.t) < self._obsolescence_time
        ]
