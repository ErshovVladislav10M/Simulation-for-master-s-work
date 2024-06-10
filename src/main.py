import json

from distributions.distribution_utils import get_distribution
from distributions.uniform.float_distribution import UniformFloatDistribution
from generators.aircraft_uav_generator import AircraftUAVGenerator
from generators.city.building_generator import CityBuildingGenerator
from generators.city.camera_generator import CameraGenerator
from generators.city.world_generator import CityWorldGenerator
from src.generators.abstract_generator import AbstractGenerator
from worlds.area import Area
from worlds.coodrinate import Coordinate


def get_building_generator(simulation_data) -> AbstractGenerator:
    with open(simulation_data["building"], "r") as file:
        building_data = json.load(file)

    return CityBuildingGenerator(
        coordinate_distribution=get_distribution(simulation_data["building_coordinate_distribution"]),
        height_distribution=get_distribution(building_data["height_distribution"]),
        side_distribution=get_distribution(building_data["side_distribution"])
    )


def get_sensor_generator(simulation_data, cube_side: float) -> AbstractGenerator:
    with open(simulation_data["sensor"], "r") as file:
        sensor_data = json.load(file)
    with open(simulation_data["uav"], "r") as file:
        uav_data = json.load(file)

    distance = uav_data["detection_distance"]
    distance_distribution = UniformFloatDistribution(min_value=distance, max_value=distance)

    return CameraGenerator(
        coordinate_distribution=get_distribution(simulation_data["sensor_coordinate_distribution"]),
        height_distribution=get_distribution(sensor_data["height_distribution"]),
        direction_vector_distribution=get_distribution(sensor_data["direction_vector_distribution"]),
        distance_distribution=distance_distribution,
        alpha=sensor_data["alpha"],
        beta=sensor_data["beta"],
        cube_side=cube_side,
        initial_q=0.2,
        obsolescence_time=1
    )


def get_uav_generator(simulation_data) -> AbstractGenerator:
    with open(simulation_data["uav"], "r") as file:
        uav_data = json.load(file)

    return AircraftUAVGenerator(
        start_coordinate_distribution=get_distribution(simulation_data["uav_coordinate_distribution"]),
        start_direction_vector_distribution=get_distribution(uav_data["start_direction_vector_distribution"]),
        speed_distribution=get_distribution(uav_data["speed_distribution"]),
        keep_start_vector=True,
        num_of_steps=simulation_data["num_of_steps"],
        world_size=simulation_data["world_size"]
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
    with open("src/configurations/simulations/mavic3_h20.json", "r") as file:
        simulation_data = json.load(file)

    world = CityWorldGenerator(
        simulation_data=simulation_data,
        create_step_images=simulation_data["create_step_images"],
        # exclude_areas=get_exclude_areas(),
        exclude_areas=[],
        building_generator=get_building_generator(simulation_data),
        camera_generator=get_sensor_generator(simulation_data, cube_side),
        uav_generator=get_uav_generator(simulation_data)
    ).create()[0]

    world.run()


if __name__ == "__main__":
    for cube_side in [10, 15]:
        main(cube_side)
    # main(5)
