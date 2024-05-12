import math

from distributions.norm.float_distribution import NormFloatDistribution
from distributions.uniform.coordinate_distribution import UniformCoordinateDistribution
from distributions.uniform.float_distribution import UniformFloatDistribution
from distributions.uniform.vector_distribution import UniformVectorDistribution
from generators.aircraft_uav_generator import AircraftUAVGenerator
from generators.city.building_generator import CityBuildingGenerator
from generators.city.camera_generator import CameraGenerator
from generators.city.world_generator import CityWorldGenerator
from sensors.cameras.camera import Camera
from uavs.uav import UAV
from worlds.area import Area
from worlds.coodrinate import Coordinate
from worlds.vector import Vector


def get_building_generator() -> CityBuildingGenerator:
    coordinate_distribution = UniformCoordinateDistribution(
        min_value=Coordinate(-150, -150, 0),
        max_value=Coordinate(150, 150, 0)
    )
    height_distribution = NormFloatDistribution(peek=20, scale=5)
    side_distribution = NormFloatDistribution(peek=15, scale=5)

    return CityBuildingGenerator(
        coordinate_distribution=coordinate_distribution,
        height_distribution=height_distribution,
        side_distribution=side_distribution
    )


def get_camera_generator() -> CameraGenerator:
    coordinate_distribution = UniformCoordinateDistribution(
        min_value=Coordinate(-150, -150, 0),
        max_value=Coordinate(150, 150, 0)
    )
    height_distribution = NormFloatDistribution(peek=20, scale=5)
    vector_distribution = UniformVectorDistribution(
        min_value=Vector(-80, -80, 0),
        max_value=Vector(80, 80, 0)
    )
    distance_distribution = UniformFloatDistribution(min_value=100, max_value=100)

    return CameraGenerator(
        coordinate_distribution=coordinate_distribution,
        height_distribution=height_distribution,
        vector_distribution=vector_distribution,
        distance_distribution=distance_distribution,
        alpha=2 * math.pi / 3,
        beta=math.pi / 2,
        cube_side=4,
        initial_q=0.2,
        obsolescence_time=1
    )


def get_uav_generator(num_of_steps: int) -> AircraftUAVGenerator:
    coordinate_distribution = UniformCoordinateDistribution(
        min_value=Coordinate(-170, -170, 10),
        max_value=Coordinate(170, 170, 11)
    )
    vector_distribution = UniformVectorDistribution(
        min_value=Vector(-10, -10, 0),
        max_value=Vector(10, 10, 0)
    )

    return AircraftUAVGenerator(
        start_coordinate_distribution=coordinate_distribution,
        start_vector_distribution=vector_distribution,
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

    world = CityWorldGenerator(
        num_of_steps=num_of_steps,
        world_size=200,
        create_step_images=True,
        exclude_areas=get_exclude_areas(),
        cube_side_size=1,
        building_generator=get_building_generator(),
        camera_generator=get_camera_generator(),
        uav_generator=get_uav_generator(num_of_steps)
    ).create()[0]

    # camera = Camera(
    #     id=1,
    #     coordinate=Coordinate(10, 10, 10),
    #     vector=Vector(10, 10, 0),
    #     alpha=0.25 * math.pi,
    #     beta=0.25 * math.pi,
    #     cube_side=4,
    #     initial_q=0.6,
    #     obsolescence_time=1
    # )
    # world.cameras.append(camera)
    #
    # route = [
    #     Coordinate(11, 11, 10),
    #     Coordinate(12, 12, 10),
    #     Coordinate(13, 13, 10),
    #     Coordinate(14, 14, 10),
    #     Coordinate(15, 15, 10),
    #     Coordinate(16, 16, 10),
    #     Coordinate(17, 17, 10),
    #     Coordinate(18, 18, 10),
    #     Coordinate(19, 19, 10),
    # ]
    # world.uavs.append(UAV(route=route))

    world.run()
