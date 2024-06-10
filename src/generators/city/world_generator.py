from src.generators.abstract_generator import AbstractGenerator
from src.worlds.abstract_world_object import AbstractWorldObject
from src.worlds.area import Area
from src.worlds.city.world import CityWorld
from src.worlds.coodrinate import Coordinate


class CityWorldGenerator(AbstractGenerator):

    def __init__(
        self,
        simulation_data,
        exclude_areas: list[Area],
        building_generator: AbstractGenerator,
        camera_generator: AbstractGenerator,
        uav_generator: AbstractGenerator
    ):
        self._simulation_data = simulation_data
        self._create_step_images = simulation_data["create_step_images"]
        self._exclude_areas = exclude_areas
        self._building_generator = building_generator
        self._camera_generator = camera_generator
        self._uav_generator = uav_generator

    def create(self, num_of_objects=1) -> list[CityWorld]:
        world = CityWorld(
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
