from __future__ import annotations

import math

import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path

from src.worlds.abstract_world_object import AbstractWorldObject
from src.worlds.coodrinate import Coordinate
from src.worlds.vector import Vector


class UAV(AbstractWorldObject):

    def __init__(self, type: str, route: list[Coordinate]):
        self.type = type
        self.route = route
        self.step = 0
        super().__init__()

    def create_xy_patch(self) -> PathPatch | None:
        coordinate = self.get_coordinate()
        next_coordinate = self.get_next_coordinate()

        if coordinate is None or next_coordinate is None:
            return None

        guide_vector = Vector(next_coordinate.x - coordinate.x, next_coordinate.y - coordinate.y, 0)
        norm_vector = guide_vector / guide_vector.length()
        central_coordinate = coordinate + norm_vector * 10

        left_vector = norm_vector.rotate(alpha=0.25 * math.pi, beta=0)
        left_coordinate = coordinate + left_vector * 4

        right_vector = norm_vector.rotate(alpha=-0.25 * math.pi, beta=0)
        right_coordinate = coordinate + right_vector * 4

        vertices = np.array(
            [
                (left_coordinate.x, left_coordinate.y),
                (central_coordinate.x, central_coordinate.y),
                (right_coordinate.x, right_coordinate.y),
                (left_coordinate.x, left_coordinate.y)
            ]
        )
        path = Path(vertices=vertices)

        return PathPatch(
            path,
            fill=False,
            edgecolor="red"
        )

    def do_step(self) -> None:
        if not self.is_finished():
            self.step += 1

    def is_finished(self) -> bool:
        return len(self.route) <= self.step

    def get_coordinate(self) -> Coordinate | None:
        if not self.is_finished():
            return self.route[self.step]

        return None

    def get_next_coordinate(self) -> Coordinate | None:
        if len(self.route) > self.step + 1:
            return self.route[self.step + 1]

        return None
