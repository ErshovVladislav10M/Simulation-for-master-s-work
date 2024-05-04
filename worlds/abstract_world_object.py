from abc import ABC, abstractmethod

from matplotlib.patches import Patch

from worlds.coodrinate import Coordinate


class AbstractWorldObject(ABC):

    def __init__(self):
        self._patch = self.create_patch()

    @abstractmethod
    def create_patch(self) -> Patch:
        ...

    def contain(self, coordinate: Coordinate, radius: float = 0) -> bool:
        return self._patch.contains_point(point=(coordinate.x, coordinate.y), radius=radius)
