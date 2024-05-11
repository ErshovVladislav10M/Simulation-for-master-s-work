from distributions.abstract_distribution import AbstractDistribution
from generators.abstract_generator import AbstractGenerator
from worlds.city.building import CityBuilding


class CityBuildingGenerator(AbstractGenerator):

    def __init__(
        self,
        coordinate_distribution: AbstractDistribution,
        height_distribution: AbstractDistribution,
        side_distribution: AbstractDistribution
    ):
        self._coordinate_distribution = coordinate_distribution
        self._height_distribution = height_distribution
        self._side_distribution = side_distribution

    def create(self, num_of_objects: int = 1) -> list[CityBuilding]:
        return [
            CityBuilding(coordinate, height, side)
            for coordinate, height, side in zip(
                self._coordinate_distribution.get_values(num_of_objects),
                self._height_distribution.get_values(num_of_objects),
                self._side_distribution.get_values(num_of_objects),
            )
        ]
