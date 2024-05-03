from generators.square.building_generator import SquareBuildingGenerator
from generators.square.world_generator import SquareWorldGenerator
from worlds.area import Area
from worlds.coodrinate import Coordinate
from worlds.cube import Cube


if __name__ == "__main__":
    build_generator = SquareBuildingGenerator(
        min_x=-100,
        max_x=100,
        min_y=-100,
        max_y=100,
        average_height=20,
        min_height=5,
        max_height=100,
        average_side=15,
        min_side=10,
        max_side=50,
        num_of_buildings=50
    )
    world_vertices = [
        Coordinate(-70, -70),
        Coordinate(-30, 0),
        Coordinate(-70, 70),
        Coordinate(70, 70),
        Coordinate(140, 0),
        Coordinate(70, -70)
    ]
    world = SquareWorldGenerator(
        num_steps=10,
        create_step_images=True,
        world_vertices=world_vertices,
        cube_side_size=1,
        building_generator=build_generator
    ).create()

    # route = [Cube(x, x, x) for x in range(8)]
    # world.create_uav(route=route)

    # area_cubes = []
    # for i in range(1, 8):
    #     for j in range(i, 8):
    #         # for k in range(8):
    #         area_cubes.append(Cube(i, j, 0))
    # area = Area(area_cubes)
    # camera = world.create_camera(area=area, position=Cube(0, 1, 1), initial_q=0.3, obsolescence_time=4)

    world.run()

    # print(camera.get_all_measurements())
