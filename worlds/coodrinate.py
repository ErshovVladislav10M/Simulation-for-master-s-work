import numpy as np


class Coordinate:

    def __init__(self, x: float, y: float, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other) -> bool:
        if not isinstance(other, Coordinate):
            return False

        return np.isclose(self.x, other.x)\
            and np.isclose(self.y, other.y)\
            and np.isclose(self.z, other.z)
