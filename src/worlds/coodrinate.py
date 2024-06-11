import math

import numpy as np


class Coordinate:

    @staticmethod
    def of(coordinate: list):
        return Coordinate(coordinate[0], coordinate[1], coordinate[2])

    def __init__(self, x: float, y: float, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other) -> float:
        return math.sqrt(
            math.pow(self.x - other.x, 2)
            + math.pow(self.y - other.y, 2)
            + math.pow(self.z - other.z, 2)
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Coordinate):
            return False

        return np.isclose(self.x, other.x)\
            and np.isclose(self.y, other.y)\
            and np.isclose(self.z, other.z)

    def __add__(self, other):
        if isinstance(other, Coordinate):
            return Coordinate(
                self.x + other.x,
                self.y + other.y,
                self.z + other.z,
            )

        if isinstance(other, float):
            return Coordinate(
                self.x + other,
                self.y + other,
                self.z + other,
            )

        raise ValueError()

    def __sub__(self, other):
        return Coordinate(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    def __mul__(self, other):
        if isinstance(other, Coordinate):
            return self.x * other.x + self.y * other.y + self.z * other.z

        return Coordinate(self.x * other, self.y * other, self.z * other)

    def __str__(self) -> str:
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"
