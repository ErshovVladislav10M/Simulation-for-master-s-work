from generators.square.building_generator import SquareBuildingGenerator
from generators.square.camera_generator import CameraGenerator
from generators.square.simple_camera_area_generator import SimpleCameraAreaGenerator
from generators.square.world_generator import SquareWorldGenerator
from sensors.cameras.camera import Camera
from worlds.area import Area
from worlds.coodrinate import Coordinate

if __name__ == "__main__":
    build_generator = SquareBuildingGenerator(
        min_x=-150,
        max_x=150,
        min_y=-150,
        max_y=150,
        average_height=20,
        min_height=5,
        max_height=100,
        average_side=15,
        min_side=10,
        max_side=50,
        num_of_buildings=100
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
        average_height=20,
        min_height=5,
        max_height=100,
        num_of_cameras=100,
        initial_q=0.5,
        obsolescence_time=5
    )

    world = SquareWorldGenerator(
        num_steps=10,
        create_step_images=True,
        exclude_areas=exclude_areas,
        cube_side_size=1,
        building_generator=build_generator,
        camera_generator=camera_generator
    ).create()

    area = SimpleCameraAreaGenerator(
        start_coordinate=Coordinate(0, 0),
        radius=5,
        cube_side=0.25,
    ).create()
    camera = Camera(
        id=0,
        world=world,
        coordinate=Coordinate(0, 0),
        area=area,
        initial_q=1,
        obsolescence_time=10
    )
    world.cameras.append(camera)
    # route = [Cube(x, x, x) for x in range(8)]
    # world.create_uav(route=route)

    world.run()
