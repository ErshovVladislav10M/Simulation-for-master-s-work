from abc import ABC

from sensors.cameras.camera import Camera
from uavs.uav import UAV
from worlds.abstract_world import AbstractWorld
from worlds.area import Area
from worlds.city.building import CityBuilding
from worlds.city.drawer import CityDrawer


class CityWorld(AbstractWorld, ABC):

    def __init__(
        self,
        num_steps: int,
        size: float,
        create_step_images: bool,
        exclude_areas: list[Area],
        cube_side_size: float
    ):
        super().__init__(num_steps, size, create_step_images)
        self.buildings: list[CityBuilding] = []
        self.cameras: list[Camera] = []
        self.uavs: list[UAV] = []
        self._exclude_areas = exclude_areas
        self._cube_side_size = cube_side_size
        self._drawer = CityDrawer(
            self,
            self.buildings,
            self.cameras,
            self.uavs,
            self._exclude_areas,
            cube_side_size
        )

    def run(self) -> None:
        for _ in range(self._num_steps):
            self.actual_step += 1
            print("Step: " + str(self.actual_step))

            self.do_step()

            self.rec_messages()
            self.send_messages()

            if self._create_step_images:
                self._drawer.draw_plane(self._num_steps, self.actual_step)

    def rec_messages(self) -> None:
        pass

    def send_messages(self) -> None:
        for i_camera in self.cameras:
            for j_camera in self.cameras:
                i_camera.rec_measurements(self, j_camera.send_measurements(self))

    def do_step(self) -> None:
        for uav in self.uavs:
            uav.do_step()

        for camera in self.cameras:
            camera.do_measurement(self)

    def get_uavs(self) -> list[UAV]:
        return self.uavs
