import math

from src.worlds.coodrinate import Coordinate


class Vector(Coordinate):

    def length(self) -> float:
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def get_angle(self, other) -> float:
        self_length = math.sqrt(
            math.pow(self.x, 2)
            + math.pow(self.y, 2)
            + math.pow(self.z, 2)
        )
        other_length = math.sqrt(
            math.pow(other.x, 2)
            + math.pow(other.y, 2)
            + math.pow(other.z, 2)
        )

        return math.asin(self * other / self_length / other_length)

    def rotate(self, alpha: float, beta: float):
        x, y = self._get_vector(self.x, self.y, alpha)
        x, z = self._get_vector(x, self.z, beta)

        return Vector(x, y, z)

    @staticmethod
    def _get_vector(first: float, second: float, angle: float) -> tuple[float, float]:
        return (
            first * math.cos(angle) - second * math.sin(angle),
            second * math.cos(angle) + first * math.sin(angle)
        )

    @staticmethod
    def of(coordinate: Coordinate):
        return Vector(coordinate.x, coordinate.y, coordinate.z)

    def __mul__(self, other):
        if isinstance(other, Coordinate):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float):
        return Vector(self.x / other, self.y / other, self.z / other)

    def __floordiv__(self, other: float):
        return Vector(self.x // other, self.y // other, self.z // other)
