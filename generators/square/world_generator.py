from generators.abstract_generator import AbstractGenerator
from generators.square.building_generator import SquareBuildingGenerator
from worlds.abstract_world_object import AbstractWorldObject
from worlds.area import Area
from worlds.coodrinate import Coordinate
from worlds.square.world import SquareWorld


class SquareWorldGenerator(AbstractGenerator):

    def __init__(
        self,
        num_steps: int,
        create_step_images: bool,
        exclude_areas: list[Area],
        cube_side_size: float,
        building_generator: SquareBuildingGenerator
    ):
        self._num_steps = num_steps
        self._create_step_images = create_step_images
        self._exclude_areas = exclude_areas
        self._cube_side_size = cube_side_size
        self._building_generator = building_generator

    def create(self) -> SquareWorld:
        world = SquareWorld(
            self._num_steps,
            self._create_step_images,
            self._exclude_areas,
            self._cube_side_size
        )

        for building in self._building_generator.create():
            if self._check_on_contains(building.coordinate, building.side, self._exclude_areas):
                continue

            if self._check_on_contains(building.coordinate, building.side, world.get_buildings()):
                continue

            world.get_buildings().append(building)

        return world

    @staticmethod
    def _check_on_contains(
        coordinate: Coordinate,
        radius: float,
        old_objects: list[AbstractWorldObject]
    ) -> bool:
        for old_object in old_objects:
            if old_object.contain(coordinate, radius):
                return True

        return False
