import math

from worlds.coodrinate import Coordinate


class Vector(Coordinate):

    def length(self) -> float:
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def get_angle(self, other) -> float:
        vector_1_length = math.sqrt(
            math.pow(self.x, 2)
            + math.pow(self.y, 2)
            + math.pow(self.z, 2)
        )
        vector_2_length = math.sqrt(
            math.pow(other.x, 2)
            + math.pow(other.y, 2)
            + math.pow(other.z, 2)
        )

        return math.asin(
            self * other / vector_1_length / vector_2_length
        )

    #TODO: update for 3 coordinates
    @staticmethod
    def get_vector(first: float, second: float, angle: float) -> tuple[float, float]:
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
            return Coordinate(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float):
        return Vector(self.x / other, self.y / other, self.z / other)

    def __floordiv__(self, other: float):
        return Vector(self.x // other, self.y // other, self.z // other)
