import math

from worlds.coodrinate import Coordinate


class Vector(Coordinate):

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
