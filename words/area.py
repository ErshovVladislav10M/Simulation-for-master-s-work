from uavs.uav import UAV


class Area:

    def __init__(self, uavs: list[UAV]):
        self._uavs = uavs

    def do_step(self):
        for uav in self._uavs:
            uav.do_step()

    def get_actual_uavs(self):
        return [uav for uav in self._uavs if not uav.is_finished()]
