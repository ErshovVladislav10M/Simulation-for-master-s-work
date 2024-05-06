from matplotlib.patches import Circle

from measurements.measurement import Measurement
from worlds.abstract_world import AbstractWorld
from worlds.abstract_world_object import AbstractWorldObject
from worlds.coodrinate import Coordinate
from sensors.cube_area import CubeArea


class Camera(AbstractWorldObject):

    def __init__(
        self,
        id: int,
        coordinate: Coordinate,
        area: CubeArea,
        initial_q: float,
        obsolescence_time: int
    ):
        self.id = id
        self.coordinate = coordinate
        self._area = area
        self._measurements = []
        self._initial_q = initial_q
        self._obsolescence_time = obsolescence_time
        super().__init__()

    def create_patch(self) -> Circle:
        return Circle(
            xy=(self.coordinate.x, self.coordinate.y),
            radius=0.2,
            edgecolor="blue",
        )

    def do_measurement(self, world: AbstractWorld) -> None:
        uavs_in_area = [
            uav
            for uav in world.get_uavs()
            if self._area.contain(uav.get_coordinate())
        ]

        for uav in uavs_in_area:
            cube = (uav.get_coordinate(), self._initial_q)
            measurement = Measurement([cube], world.actual_step)
            self._measurements.append(measurement)

    def get_all_measurements(self) -> list[Measurement]:
        return self._measurements

    def get_actual_measurements(self, actual_step: int) -> list[Measurement]:
        return [
            measurement
            for measurement in self._measurements
            if abs(actual_step - measurement.t) < self._obsolescence_time
        ]
