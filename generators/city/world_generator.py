from generators.abstract_generator import AbstractGenerator
from generators.aircraft_uav_generator import AircraftUAVGenerator
from generators.city.building_generator import SquareBuildingGenerator
from generators.city.camera_generator import CameraGenerator
from worlds.abstract_world_object import AbstractWorldObject
from worlds.area import Area
from worlds.coodrinate import Coordinate
from worlds.city.world import CityWorld


class CityWorldGenerator(AbstractGenerator):

    def __init__(
        self,
        num_steps: int,
        create_step_images: bool,
        exclude_areas: list[Area],
        cube_side_size: float,
        building_generator: SquareBuildingGenerator,
        camera_generator: CameraGenerator,
        uav_generator: AircraftUAVGenerator
    ):
        self._num_steps = num_steps
        self._create_step_images = create_step_images
        self._exclude_areas = exclude_areas
        self._cube_side_size = cube_side_size
        self._building_generator = building_generator
        self._camera_generator = camera_generator
        self._uav_generator = uav_generator

    def create(self, num_of_objects=1) -> list[CityWorld]:
        world = CityWorld(
            self._num_steps,
            self._create_step_images,
            self._exclude_areas,
            self._cube_side_size
        )

        for building in self._building_generator.create(100):
            if self._check_on_contains(building.coordinate, building.side, self._exclude_areas):
                continue

            if self._check_on_contains(building.coordinate, building.side, world.buildings):
                continue

            world.buildings.append(building)

        for camera in self._camera_generator.create(100):
            world.cameras.append(camera)

        for uav in self._uav_generator.create(10):
            world.uavs.append(uav)

        return [world]

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
