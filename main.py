from measurements.cube import Cube
from worlds.area import Area
from worlds.world import World


if __name__ == "__main__":
    world = World(num_steps=10, create_step_images=True)

    route = [Cube(x, x, x) for x in range(8)]
    world.create_uav(route=route)

    area = Area([Cube(1, 1, 1), Cube(2, 2, 2), Cube(3, 3, 3)])
    camera = world.create_camera(area=area, position=Cube(0, 1, 1), initial_q=0.3, obsolescence_time=4)

    world.run()

    print(camera.get_all_measurements())
