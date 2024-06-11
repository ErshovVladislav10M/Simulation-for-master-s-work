import json

from src.distributions.distribution_utils import get_distribution
from src.distributions.uniform.float_distribution import UniformFloatDistribution
from src.generators.aircraft_uav_generator import AircraftUAVGenerator
from src.generators.city.building_generator import CityBuildingGenerator
from src.generators.city.camera_generator import CameraGenerator
from src.generators.city.world_generator import CityWorldGenerator
from src.generators.abstract_generator import AbstractGenerator
from src.worlds.area import Area
from src.worlds.coodrinate import Coordinate


def get_building_generator(simulation_data) -> AbstractGenerator:
    with open(simulation_data["building"], "r", encoding="utf-8") as file:
        building_data = json.load(file)

    return CityBuildingGenerator(
        coordinate_distribution=get_distribution(simulation_data["building_coordinate_distribution"]),
        height_distribution=get_distribution(building_data["height_distribution"]),
        side_distribution=get_distribution(building_data["side_distribution"])
    )


def get_sensor_generator(simulation_data, cube_side: float) -> AbstractGenerator:
    with open(simulation_data["sensor"], "r", encoding="utf-8") as file:
        sensor_data = json.load(file)
    with open(simulation_data["uav"], "r", encoding="utf-8") as file:
        uav_data = json.load(file)

    distance = uav_data["detection_distance"]
    distance_distribution = UniformFloatDistribution(min_value=distance, max_value=distance)

    return CameraGenerator(
        coordinate_distribution=get_distribution(simulation_data["sensor_coordinate_distribution"]),
        distance_distribution=distance_distribution,
        sensor_data=sensor_data,
        cube_side=cube_side,
        obsolescence_time=1
    )


def get_uav_generator(simulation_data) -> AbstractGenerator:
    with open(simulation_data["uav"], "r", encoding="utf-8") as file:
        uav_data = json.load(file)

    return AircraftUAVGenerator(
        simulation_data=simulation_data,
        uav_data=uav_data,
        keep_start_vector=True
    )


def get_exclude_areas() -> list[Area]:
    return [
        Area(
            [
                Coordinate(-200, 160),
                Coordinate(-170, 140),
                Coordinate(-150, 130),
                Coordinate(-130, 100),
                Coordinate(-90, 90),
                Coordinate(-60, 80),
                Coordinate(-50, 60),
                Coordinate(20, 10),
                Coordinate(60, 0),
                Coordinate(80, -30),
                Coordinate(110, -40),
                Coordinate(140, -40),
                Coordinate(160, -70),
                Coordinate(200, -80),
                Coordinate(200, -50),
                Coordinate(160, -30),
                Coordinate(140, -10),
                Coordinate(110, -10),
                Coordinate(80, 0),
                Coordinate(60, 30),
                Coordinate(20, 40),
                Coordinate(-50, 90),
                Coordinate(-60, 110),
                Coordinate(-90, 120),
                Coordinate(-130, 130),
                Coordinate(-150, 160),
                Coordinate(-170, 170),
                Coordinate(-200, 190),
            ]
        )
    ]


def main(cube_side: float):
    with open("./configurations/simulations/mavic3_h20.json", "r", encoding="utf-8") as file:
        simulation_data = json.load(file)

    world = CityWorldGenerator(
        simulation_data=simulation_data,
        # exclude_areas=get_exclude_areas(),
        exclude_areas=[],
        building_generator=get_building_generator(simulation_data),
        camera_generator=get_sensor_generator(simulation_data, cube_side),
        uav_generator=get_uav_generator(simulation_data)
    ).create()[0]

    world.run()


if __name__ == "__main__":
    for side in [10, 15]:
        main(side)
    # main(5)
