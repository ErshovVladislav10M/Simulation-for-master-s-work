import json

from distributions.norm.float_distribution import NormFloatDistribution
from distributions.uniform.coordinate_distribution import UniformCoordinateDistribution
from distributions.uniform.float_distribution import UniformFloatDistribution
from distributions.uniform.vector_distribution import UniformVectorDistribution
from generators.aircraft_uav_generator import AircraftUAVGenerator
from generators.city.building_generator import CityBuildingGenerator
from generators.city.camera_generator import CameraGenerator
from generators.city.world_generator import CityWorldGenerator
from worlds.area import Area
from worlds.coodrinate import Coordinate
from worlds.vector import Vector


def get_building_generator(simulation_data) -> CityBuildingGenerator:
    world_size = simulation_data["world_size"]

    coordinate_distribution = UniformCoordinateDistribution(
        min_value=Coordinate(-world_size, -world_size, 0),
        max_value=Coordinate(world_size, world_size, 0)
    )
    height_distribution = NormFloatDistribution(peek=20, scale=5)
    side_distribution = NormFloatDistribution(peek=20, scale=5)

    return CityBuildingGenerator(
        coordinate_distribution=coordinate_distribution,
        height_distribution=height_distribution,
        side_distribution=side_distribution
    )


def get_camera_generator(simulation_data, cube_side: float) -> CameraGenerator:
    with open(simulation_data["sensor"], "r") as file:
        sensor_data = json.load(file)
    with open(simulation_data["uav"], "r") as file:
        uav_data = json.load(file)

    world_size = simulation_data["world_size"]
    coordinate_distribution = UniformCoordinateDistribution(
        min_value=Coordinate(-world_size, -world_size, 0),
        max_value=Coordinate(world_size, world_size, 0)
    )
    height_distribution = NormFloatDistribution(peek=sensor_data["peek_height"], scale=sensor_data["scale_height"])
    vector_distribution = UniformVectorDistribution(
        min_value=Vector(-1, -1, -0.33),
        max_value=Vector(1, 1, 0)
    )
    distance = uav_data["detection_distance"]
    distance_distribution = UniformFloatDistribution(min_value=distance, max_value=distance)

    return CameraGenerator(
        coordinate_distribution=coordinate_distribution,
        height_distribution=height_distribution,
        vector_distribution=vector_distribution,
        distance_distribution=distance_distribution,
        alpha=sensor_data["alpha"],
        beta=sensor_data["beta"],
        cube_side=cube_side,
        initial_q=0.2,
        obsolescence_time=1
    )


def get_uav_generator(simulation_data) -> AircraftUAVGenerator:
    world_size = simulation_data["world_size"]
    num_of_steps = simulation_data["num_of_steps"]
    initial_height = simulation_data["uav_initial_height"]

    coordinate_distribution = UniformCoordinateDistribution(
        min_value=Coordinate(-world_size, -world_size, initial_height),
        max_value=Coordinate(world_size, world_size, initial_height)
    )
    vector_distribution = UniformVectorDistribution(
        min_value=Vector(-1, -1, 0),
        max_value=Vector(1, 1, 0)
    )

    with open(simulation_data["uav"], "r") as file:
        uav_data = json.load(file)
    speed = uav_data["speed"]
    speed_distribution = UniformFloatDistribution(min_value=speed, max_value=speed)

    return AircraftUAVGenerator(
        start_coordinate_distribution=coordinate_distribution,
        start_vector_distribution=vector_distribution,
        speed_distribution=speed_distribution,
        keep_start_vector=True,
        num_of_steps=num_of_steps,
        world_size=world_size
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
    with open("configurations/simulations/for_presentation.json", "r") as file:
        simulation_data = json.load(file)

    world = CityWorldGenerator(
        simulation_data=simulation_data,
        create_step_images=simulation_data["create_step_images"],
        # exclude_areas=get_exclude_areas(),
        exclude_areas=[],
        building_generator=get_building_generator(simulation_data),
        camera_generator=get_camera_generator(simulation_data, cube_side),
        uav_generator=get_uav_generator(simulation_data)
    ).create()[0]

    world.run()


if __name__ == "__main__":
    for cube_side in [10, 15]:
        main(cube_side)
    # main(5)
