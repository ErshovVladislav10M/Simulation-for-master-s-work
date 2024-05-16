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


def get_building_generator(world_size: float) -> CityBuildingGenerator:
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


def get_camera_generator(world_size: float, distance: float) -> CameraGenerator:
    with open("configurations/cameras/safe_city_camera.json", "r") as file:
        data = json.load(file)

    coordinate_distribution = UniformCoordinateDistribution(
        min_value=Coordinate(-world_size, -world_size, 0),
        max_value=Coordinate(world_size, world_size, 0)
    )
    height_distribution = NormFloatDistribution(peek=data["peek_height"], scale=data["scale_height"])
    vector_distribution = UniformVectorDistribution(
        min_value=Vector(-1, -1, -0.33),
        max_value=Vector(1, 1, 0)
    )
    distance_distribution = UniformFloatDistribution(min_value=distance, max_value=distance)

    return CameraGenerator(
        coordinate_distribution=coordinate_distribution,
        height_distribution=height_distribution,
        vector_distribution=vector_distribution,
        distance_distribution=distance_distribution,
        alpha=data["alpha"],
        beta=data["beta"],
        cube_side=10,
        initial_q=0.2,
        obsolescence_time=1
    )


def get_uav_generator(world_size: float, initial_height: float, num_of_steps: int) -> AircraftUAVGenerator:
    coordinate_distribution = UniformCoordinateDistribution(
        min_value=Coordinate(-world_size, -world_size, initial_height),
        max_value=Coordinate(world_size, world_size, initial_height)
    )
    vector_distribution = UniformVectorDistribution(
        min_value=Vector(-1, -1, 0),
        max_value=Vector(1, 1, 0)
    )

    with open("configurations/uavs/cavok.json", "r") as file:
        data = json.load(file)
    speed = data["speed"]
    speed_distribution = UniformFloatDistribution(min_value=speed, max_value=speed)

    return AircraftUAVGenerator(
        start_coordinate_distribution=coordinate_distribution,
        start_vector_distribution=vector_distribution,
        speed_distribution=speed_distribution,
        keep_start_vector=True,
        num_of_steps=num_of_steps
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


if __name__ == "__main__":
    num_of_steps = 40
    world_size = 2000

    world = CityWorldGenerator(
        num_of_steps=num_of_steps,
        world_size=world_size,
        create_step_images=False,
        # exclude_areas=get_exclude_areas(),
        exclude_areas=[],
        building_generator=get_building_generator(world_size),
        camera_generator=get_camera_generator(world_size=world_size, distance=150),
        uav_generator=get_uav_generator(world_size=world_size, initial_height=10, num_of_steps=num_of_steps)
    ).create()[0]

    world.run()
