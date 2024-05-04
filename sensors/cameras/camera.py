
from measurements.measurement import Measurement
from worlds.abstract_world import AbstractWorld
from worlds.coodrinate import Coordinate
from sensors.cube_area import CubeArea


class Camera:

    def __init__(
        self,
        id: int,
        world: AbstractWorld,
        coordinate: Coordinate,
        area: CubeArea,
        initial_q: float,
        obsolescence_time: int
    ):
        self.id = id
        self._world = world
        self.coordinate = coordinate
        self._area = area
        self._measurements = []
        self._initial_q = initial_q
        self._obsolescence_time = obsolescence_time

    def do_measurement(self) -> None:
        uavs_in_area = [
            uav
            for uav in self._world.get_uavs()
            if self._area.contain(uav.get_coordinate())
        ]

        for uav in uavs_in_area:
            cube = (uav.get_coordinate(), self._initial_q)
            measurement = Measurement([cube], self._world.actual_step)
            self._measurements.append(measurement)

    def get_all_measurements(self) -> list[Measurement]:
        return self._measurements

    def get_actual_measurements(self) -> list[Measurement]:
        return [
            measurement
            for measurement in self._measurements
            if abs(self._world.actual_step - measurement.t) < self._obsolescence_time
        ]