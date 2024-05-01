from measurements.measurement import Measurement
from worlds.abstract_world import AbstractWorld
from worlds.area import Area


class Camera:

    def __init__(self, world: AbstractWorld, area: Area, initial_q: float):
        self._world = world
        self._area = area
        self._measurements = []
        self._initial_q = initial_q

    def do_measurement(self) -> None:
        uavs_in_area = [uav for uav in self._world.get_uavs() if self._area.contain(uav)]
        for uav in uavs_in_area:
            cube = (uav.get_position(), self._initial_q)
            measurement = Measurement([cube], self._world.actual_step)
            self._measurements.append(measurement)

    def get_actual_measurements(self) -> list[Measurement]:
        return self._measurements
        # return [measurement for measurement in self._measurements if measurement.t]
