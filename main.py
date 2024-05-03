from generators.world_generator import WorldGenerator
from worlds.area import Area
from worlds.coodrinate import Coordinate
from worlds.cube import Cube


if __name__ == "__main__":
    world_vertices = [Coordinate(-7, -7), Coordinate(7, -7), Coordinate(7, 7), Coordinate(-7, 7)]
    world = WorldGenerator(
        num_steps=10,
        create_step_images=True,
        world_vertices=world_vertices,
        cube_side_size=1
    ).create()

    route = [Cube(x, x, x) for x in range(8)]
    world.create_uav(route=route)

    area_cubes = []
    for i in range(1, 8):
        for j in range(i, 8):
            # for k in range(8):
            area_cubes.append(Cube(i, j, 0))
    area = Area(area_cubes)
    camera = world.create_camera(area=area, position=Cube(0, 1, 1), initial_q=0.3, obsolescence_time=4)

    world.run()

    print(camera.get_all_measurements())
