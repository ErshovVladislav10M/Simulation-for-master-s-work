from abc import ABC

from src.sensors.cameras.camera import Camera
from src.uavs.uav import UAV
from src.worlds.abstract_world import AbstractWorld
from src.worlds.area import Area
from src.worlds.city.building import CityBuilding
from src.worlds.city.drawer import CityDrawer
from src.worlds.city.listener import CityListener


class CityWorld(AbstractWorld, ABC):

    def __init__(self, exclude_areas: list[Area], simulation_data):
        super().__init__(
            simulation_data["num_of_steps"],
            simulation_data["world_size"],
            simulation_data["create_step_images"]
        )
        self.buildings: list[CityBuilding] = []
        self.cameras: list[Camera] = []
        self.uavs: list[UAV] = []
        self._exclude_areas = exclude_areas
        self._listener = CityListener(
            self,
            self.buildings,
            self.cameras,
            self.uavs,
            "src/results/" + simulation_data["name"]
        )
        self._drawer = CityDrawer(
            self,
            self.buildings,
            self.cameras,
            self.uavs,
            self._exclude_areas,
            "src/results/" + simulation_data["name"]
        )

    def run(self) -> None:
        for _ in range(self._num_of_steps):
            self.actual_step += 1
            print("Step: " + str(self.actual_step))

            self.do_step()

            self.rec_messages()
            self.send_messages()

            self._listener.detect(self._num_of_steps, self.actual_step)
            if self._create_step_images:
                self._drawer.draw_plane(self.actual_step)

    def rec_messages(self) -> None:
        pass

    def send_messages(self) -> None:
        for i_camera in self.cameras:
            for j_camera in self.cameras:
                if i_camera.coordinate.distance(j_camera.coordinate) < i_camera.distance * 2:
                    i_camera.rec_measurements(self, j_camera.send_measurements(self))

    def do_step(self) -> None:
        for uav in self.uavs:
            uav.do_step()

        for camera in self.cameras:
            camera.do_measurement(self)

    def get_uavs(self) -> list[UAV]:
        return self.uavs
