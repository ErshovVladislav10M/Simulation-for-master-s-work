from abc import ABC

from measurements.cube import Cube
from sensors.camera import Camera
from uavs.uav import UAV
from worlds.abstract_world import AbstractWorld
from worlds.area import Area


class World(AbstractWorld, ABC):

    def __init__(self, num_steps: int, create_step_images: bool):
        super().__init__(num_steps=num_steps, create_step_images=create_step_images)
        self.cameras = []
        self.uavs = []

    def run(self) -> None:
        for _ in range(self._num_steps):
            self.actual_step += 1
            print("Step: " + str(self.actual_step))

            self.do_step()

            self.rec_messages()
            self.sent_messages()
            # self.drawer.draw_plane(self.num_steps, step)

    def rec_messages(self) -> None:
        pass

    def sent_messages(self) -> None:
        pass

    def do_step(self) -> None:
        for uav in self.uavs:
            uav.do_step()

        for camera in self.cameras:
            camera.do_measurement()

    def get_uavs(self) -> list[UAV]:
        return self.uavs

    def create_camera(self, area: Area, initial_q) -> Camera:
        camera = Camera(self, area=area, initial_q=initial_q)
        self.cameras.append(camera)

        return camera

    def create_uav(self, route: list[Cube]) -> UAV:
        uav = UAV(route=route)
        self.uavs.append(uav)

        return uav
