from __future__ import annotations

from worlds.cube import Cube


class UAV:

    def __init__(self, route: list[Cube]):
        self.route = route
        self.step = 0

    def do_step(self) -> None:
        if not self.is_finished():
            self.step += 1

    def is_finished(self) -> bool:
        return len(self.route) <= self.step

    def get_position(self) -> Cube | None:
        if not self.is_finished():
            return self.route[self.step]
        else:
            return None

    def get_next_position(self) -> Cube | None:
        if len(self.route) > self.step + 1:
            return self.route[self.step + 1]
        else:
            return None
