from abc import ABC, abstractmethod

from matplotlib.patches import Patch

from src.worlds.coodrinate import Coordinate


class AbstractWorldObject(ABC):

    def __init__(self):
        self._xy_patch = self.create_xy_patch()
        self._xz_patch = self.create_xz_patch()
        self._yz_patch = self.create_yz_patch()

    @abstractmethod
    def create_xy_patch(self) -> Patch | None:
        ...

    def create_xz_patch(self) -> Patch | None:
        return None

    def create_yz_patch(self) -> Patch | None:
        return None

    def contain(self, coordinate: Coordinate, radius: float = 0) -> bool:
        if self._xy_patch is None:
            return True

        if not self._xy_patch.contains_point(point=(coordinate.x, coordinate.y), radius=radius):
            return False

        if self._xz_patch is None:
            return True

        if not self._xz_patch.contains_point(point=(coordinate.x, coordinate.z), radius=radius):
            return False

        if self._yz_patch is None:
            return True

        return self._yz_patch.contains_point(point=(coordinate.y, coordinate.z), radius=radius)
