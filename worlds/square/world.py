from abc import ABC

from worlds.coodrinate import Coordinate
from worlds.cube import Cube
from sensors.camera import Camera
from uavs.uav import UAV
from worlds.abstract_world import AbstractWorld
from worlds.area import Area
from worlds.square.drawer import SquareDrawer
from worlds.square.building import SquareBuilding


class SquareWorld(AbstractWorld, ABC):

    def __init__(
        self,
        num_steps: int,
        create_step_images: bool,
        vertices: list[Coordinate],
        cube_side_size: float
    ):
        super().__init__(num_steps, create_step_images)
        self._buildings = []
        self.cameras = []
        self.uavs = []
        self._vertices = vertices
        self._cube_side_size = cube_side_size
        self._drawer = SquareDrawer(
            self._buildings,
            self.cameras,
            self.uavs,
            vertices,
            cube_side_size
        )

    def run(self) -> None:
        for _ in range(self._num_steps):
            self.actual_step += 1
            print("Step: " + str(self.actual_step))

            self.do_step()

            self.rec_messages()
            self.sent_messages()
            self._drawer.draw_plane(self._num_steps, self.actual_step)

    def rec_messages(self) -> None:
        pass

    def sent_messages(self) -> None:
        pass

    def do_step(self) -> None:
        for uav in self.uavs:
            uav.do_step()

        for camera in self.cameras:
            camera.do_measurement()

    def get_buildings(self) -> list[SquareBuilding]:
        return self._buildings

    def get_uavs(self) -> list[UAV]:
        return self.uavs

    def add_building(self) -> None:
        ...

    def create_building(self, coordinate: Coordinate, height: int, side: int) -> SquareBuilding:
        build = SquareBuilding(coordinate, height, side)
        self._buildings.append(build)

        return build

    def create_camera(self, area: Area, position: Cube, initial_q, obsolescence_time: int) -> Camera:
        camera = Camera(
            id=len(self.cameras),
            world=self,
            area=area,
            position=position,
            initial_q=initial_q,
            obsolescence_time=obsolescence_time
        )
        self.cameras.append(camera)

        return camera

    def create_uav(self, route: list[Cube]) -> UAV:
        uav = UAV(route=route)
        self.uavs.append(uav)

        return uav
