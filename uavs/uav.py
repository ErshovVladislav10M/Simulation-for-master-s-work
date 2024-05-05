from __future__ import annotations

from matplotlib.patches import Arrow

from worlds.abstract_world_object import AbstractWorldObject
from worlds.coodrinate import Coordinate


class UAV(AbstractWorldObject):

    def __init__(self, route: list[Coordinate]):
        self.route = route
        self.step = 0
        super().__init__()

    def create_patch(self) -> Arrow | None:
        coordinate = self.get_coordinate()
        next_coordinate = self.get_next_coordinate()

        if coordinate is None or next_coordinate is None:
            return None

        return Arrow(
            x=coordinate.x,
            y=coordinate.y,
            dx=next_coordinate.x - coordinate.x,
            dy=next_coordinate.y - coordinate.y,
            width=10,
            facecolor="red",
        )

    def do_step(self) -> None:
        if not self.is_finished():
            self.step += 1

    def is_finished(self) -> bool:
        return len(self.route) <= self.step

    def get_coordinate(self) -> Coordinate | None:
        if not self.is_finished():
            return self.route[self.step]
        else:
            return None

    def get_next_coordinate(self) -> Coordinate | None:
        if len(self.route) > self.step + 1:
            return self.route[self.step + 1]
        else:
            return None
