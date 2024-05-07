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
        alpha: float,
        beta: float,
        initial_q: float,
        obsolescence_time: int
    ):
        self._coordinate = coordinate
        self._vector = vector
        self._alpha = alpha
        self._beta = beta

        x, y = Vector.get_vector(self._vector.x, self._vector.y, 0.5 * self._alpha)
        self._left_coordinate = self._coordinate + Coordinate(x, y, 0)
        x, y = Vector.get_vector(self._vector.x, self._vector.y, -0.5 * self._alpha)
        self._right_coordinate = self._coordinate + Coordinate(x, y, 0)

        self._initial_q = initial_q
        self._obsolescence_time = obsolescence_time
        super().__init__(id)

    def create_patch(self) -> PathPatch:
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

    def do_measurement(self, world: AbstractWorld) -> None:
        uavs_in_area = [
            uav
            for uav in world.get_uavs()
            if self.contain(uav.get_coordinate())
        ]

        for uav in uavs_in_area:
            cube = Cube(uav.get_coordinate(), 1)
            measurement = Measurement([(cube, self._initial_q)], world.actual_step)
            self._measurements.append(measurement)

    def _contain(self, coordinate: Coordinate) -> bool:
        return np.isclose(
            self._s_triangle(self._left_coordinate, self._coordinate, self._right_coordinate),
            self._s_triangle(coordinate, self._coordinate, self._right_coordinate)
            + self._s_triangle(self._left_coordinate, coordinate, self._right_coordinate)
            + self._s_triangle(self._left_coordinate, self._coordinate, coordinate)
        )

    @staticmethod
    def _s_triangle(coordinate_1: Coordinate, coordinate_2: Coordinate, coordinate_3: Coordinate):
        side_a = coordinate_1.distance(coordinate_2)
        side_b = coordinate_2.distance(coordinate_3)
        side_c = coordinate_3.distance(coordinate_1)
        p = 0.5 * (side_a + side_b + side_c)

        return math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))

    def get_all_measurements(self) -> list[Measurement]:
        return self._measurements

    def get_actual_measurements(self, actual_step: int) -> list[Measurement]:
        return [
            measurement
            for measurement in self._measurements
            if abs(actual_step - measurement.t) < self._obsolescence_time
        ]
