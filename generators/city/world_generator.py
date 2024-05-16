from generators.abstract_generator import AbstractGenerator
from generators.aircraft_uav_generator import AircraftUAVGenerator
from generators.city.building_generator import CityBuildingGenerator
from generators.city.camera_generator import CameraGenerator
from worlds.abstract_world_object import AbstractWorldObject
from worlds.area import Area
from worlds.coodrinate import Coordinate
from worlds.city.world import CityWorld


class CityWorldGenerator(AbstractGenerator):

    def __init__(
        self,
        simulation_data,
        create_step_images: bool,
        exclude_areas: list[Area],
        building_generator: CityBuildingGenerator,
        camera_generator: CameraGenerator,
        uav_generator: AircraftUAVGenerator
    ):
        self._simulation_data = simulation_data
        self._create_step_images = create_step_images
        self._exclude_areas = exclude_areas
        self._building_generator = building_generator
        self._camera_generator = camera_generator
        self._uav_generator = uav_generator

    def create(self, num_of_objects=1) -> list[CityWorld]:
        world = CityWorld(
            self._simulation_data["num_of_steps"],
            self._simulation_data["world_size"],
            self._create_step_images,
            self._exclude_areas,
            self._simulation_data
        )

        for building in self._building_generator.create(self._simulation_data["num_of_buildings"]):
            if self._check_on_contains(building.coordinate, building.side, self._exclude_areas):
                continue

            if self._check_on_contains(building.coordinate, building.side, world.buildings):
                continue

            world.buildings.append(building)

        for camera in self._camera_generator.create(self._simulation_data["num_of_sensors"]):
            world.cameras.append(camera)

        for uav in self._uav_generator.create(self._simulation_data["num_of_uavs"]):
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
