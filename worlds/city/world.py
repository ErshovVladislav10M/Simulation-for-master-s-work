from abc import ABC

from sensors.cameras.camera import Camera
from uavs.uav import UAV
from worlds.abstract_world import AbstractWorld
from worlds.area import Area
from worlds.coodrinate import Coordinate
from worlds.city.building import CityBuilding
from worlds.city.drawer import CityDrawer


class CityWorld(AbstractWorld, ABC):

    def __init__(
        self,
        num_steps: int,
        create_step_images: bool,
        exclude_areas: list[Area],
        cube_side_size: float
    ):
        super().__init__(num_steps, create_step_images)
        self.buildings: list[CityBuilding] = []
        self.cameras: list[Camera] = []
        self.uavs: list[UAV] = []
        self._exclude_areas = exclude_areas
        self._cube_side_size = cube_side_size
        self._drawer = CityDrawer(
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
        for camera in self.cameras:
            for camera1 in self.cameras:
                camera.rec_measurements(self, camera1.send_measurements(self))

    def do_step(self) -> None:
        for uav in self.uavs:
            uav.do_step()

        for camera in self.cameras:
            camera.do_measurement(self)

    def get_uavs(self) -> list[UAV]:
        return self.uavs

    def create_building(self, coordinate: Coordinate, height: int, side: int) -> CityBuilding:
        build = CityBuilding(coordinate, height, side)
        self.buildings.append(build)

        return build

    # def create_camera(
    #     self,
    #     coordinate: Coordinate,
    #     initial_q,
    #     obsolescence_time: int
    # ) -> Camera:
    #     camera = Camera(
    #         id=len(self.cameras),
    #         coordinate=coordinate,
    #         initial_q=initial_q,
    #         obsolescence_time=obsolescence_time
    #     )
    #     self.cameras.append(camera)
    #
    #     return camera

    def create_uav(self, route: list[Coordinate]) -> UAV:
        uav = UAV(route=route)
        self.uavs.append(uav)

        return uav
