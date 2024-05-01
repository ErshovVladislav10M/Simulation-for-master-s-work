from measurements.cube import Cube
from worlds.area import Area
from worlds.world import World


if __name__ == "__main__":
    world = World(num_steps=10, create_step_images=True)

    route = [Cube(1, 1, 1), Cube(2, 2, 2), Cube(3, 3, 3)]
    world.create_uav(route=route)

    area = Area([Cube(1, 1, 1), Cube(2, 2, 2), Cube(3, 3, 3)])
    camera = world.create_camera(area=area, initial_q=0.3)

    world.run()

    print(camera.get_actual_measurements())
