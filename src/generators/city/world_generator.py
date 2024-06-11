import json

from src.distributions.distribution_utils import get_distribution
from src.generators.abstract_generator import AbstractGenerator
from src.generators.aircraft_uav_generator import AircraftUAVGenerator
from src.generators.city.building_generator import CityBuildingGenerator
from src.worlds.abstract_world_object import AbstractWorldObject
from src.worlds.area import Area
from src.worlds.city.world import CityWorld
from src.worlds.coodrinate import Coordinate


class CityWorldGenerator(AbstractGenerator):

    def __init__(
        self,
        simulation_data,
        exclude_areas: list[Area],
        camera_generator: AbstractGenerator
    ):
        self._simulation_data = simulation_data
        self._exclude_areas = exclude_areas
        self._camera_generator = camera_generator

    def create(self, num_of_objects=1) -> list[CityWorld]:
        world = CityWorld(
            self._exclude_areas,
            self._simulation_data
        )

        for building in self._get_building_generator().create(self._simulation_data["num_of_buildings"]):
            if self._check_on_contains(building.coordinate, building.side, self._exclude_areas):
                continue

            if self._check_on_contains(building.coordinate, building.side, world.buildings):
                continue

            world.buildings.append(building)

        for camera in self._camera_generator.create(self._simulation_data["num_of_sensors"]):
            world.cameras.append(camera)

        for uav in self._get_uav_generator().create(self._simulation_data["num_of_uavs"]):
            world.uavs.append(uav)

        return [world]

    def _get_building_generator(self) -> AbstractGenerator:
        with open(self._simulation_data["building"], "r", encoding="utf-8") as file:
            building_data = json.load(file)

        return CityBuildingGenerator(
            coordinate_distribution=get_distribution(self._simulation_data["building_coordinate_distribution"]),
            height_distribution=get_distribution(building_data["height_distribution"]),
            side_distribution=get_distribution(building_data["side_distribution"])
        )

    def _get_uav_generator(self) -> AbstractGenerator:
        with open(self._simulation_data["uav"], "r", encoding="utf-8") as file:
            uav_data = json.load(file)

        return AircraftUAVGenerator(
            simulation_data=self._simulation_data,
            uav_data=uav_data,
            keep_start_vector=True
        )

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
