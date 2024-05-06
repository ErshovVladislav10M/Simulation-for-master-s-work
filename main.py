from generators.aircraft_uav_generator import AircraftUAVGenerator
from generators.city.building_generator import SquareBuildingGenerator
from generators.city.camera_generator import CameraGenerator
from generators.city.world_generator import CityWorldGenerator
from worlds.area import Area
from worlds.coodrinate import Coordinate
from worlds.vector import Vector

if __name__ == "__main__":
    build_generator = SquareBuildingGenerator(
        min_x=-150,
        max_x=150,
        min_y=-150,
        max_y=150,
        peak_height=20,
        scale_height=5,
        peak_side=15,
        scale_side=5,
    )
    exclude_areas = [
        Area([
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
        ])
    ]
    camera_generator = CameraGenerator(
        min_x=-150,
        max_x=150,
        min_y=-150,
        max_y=150,
        peek_height=20,
        scale_height=5,
        initial_q=0.5,
        obsolescence_time=5
    )
    uav_generator = AircraftUAVGenerator(
        min_start_coordinate=Coordinate(-170, -170, 10),
        max_start_coordinate=Coordinate(170, 170, 150),
        min_start_vector=Vector(-10, -10, 0),
        max_start_vector=Vector(10, 10, 0),
        keep_start_vector=True,
        num_of_steps=20
    )

    world = CityWorldGenerator(
        num_steps=20,
        create_step_images=True,
        exclude_areas=exclude_areas,
        cube_side_size=1,
        building_generator=build_generator,
        camera_generator=camera_generator,
        uav_generator=uav_generator
    ).create()[0]

    # area = SimpleCameraAreaGenerator(
    #     start_coordinate=Coordinate(0, 0),
    #     radius=5,
    #     cube_side=0.25,
    # ).create()[0]
    # camera = Camera(
    #     id=0,
    #     world=world,
    #     coordinate=Coordinate(0, 0),
    #     area=area,
    #     initial_q=1,
    #     obsolescence_time=10
    # )
    # world.cameras.append(camera)
    # route = [Cube(x, x, x) for x in range(8)]
    # world.create_uav(route=route)

    world.run()
