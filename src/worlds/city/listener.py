from src.sensors.cameras.camera import Camera
from src.uavs.uav import UAV
from src.worlds.abstract_world import AbstractWorld
from src.worlds.city.building import CityBuilding


class CityListener:

    def __init__(
        self,
        world: AbstractWorld,
        buildings: list[CityBuilding],
        cameras: list[Camera],
        uavs: list[UAV],
        path_to_results: str = "results"
    ):
        self._world = world
        self._buildings = buildings
        self._cameras = cameras
        self._uavs = uavs

        self._path_to_results = path_to_results
        self._detected_uavs_counts = []
        self._actual_uavs_counts = []

    def detect(self, num_steps: int, step: int):
        cubes = self.get_cubes(step)

        actual_uavs = [
            uav
            for uav in self._uavs
            if -self._world.size < uav.get_coordinate().x < self._world.size
               and -self._world.size < uav.get_coordinate().y < self._world.size
        ]

        count_detected_uav = 0
        for uav in actual_uavs:
            for cube in cubes:
                if cube.contain(uav.get_coordinate(), radius=cube.diagonal):
                    count_detected_uav += 1
                    break

        print("Buildings " + str(len(self._buildings)))
        print("Cameras " + str(len(self._cameras)))
        print("Detected " + str(count_detected_uav) + " of " + str(len(actual_uavs)))

        self._detected_uavs_counts.append(count_detected_uav)
        self._actual_uavs_counts.append(len(actual_uavs))
        if step == num_steps - 1:
            f = open(
                self._path_to_results + "/detected_uavs_" + str(self._cameras[0].cube_side) + ".txt",
                "w",
                encoding="utf-8"
            )
            f.write(str(self._detected_uavs_counts))
            f.close()
            f = open(
                self._path_to_results + "/actual_uavs_" + str(self._cameras[0].cube_side) + ".txt",
                "w",
                encoding="utf-8"
            )
            f.write(str(self._actual_uavs_counts))
            f.close()

    def get_cubes(self, step: int):
        cubes = []
        for camera in self._cameras:
            for measurement in camera.get_actual_measurements(step):
                for cube in measurement.cubes:
                    if cube.q > 0.7:
                        cubes.append(cube)

        return cubes
