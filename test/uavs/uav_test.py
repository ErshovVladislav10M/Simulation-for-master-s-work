from src.uavs.uav import UAV
from src.worlds.coodrinate import Coordinate


def test():
    uav_type = "micro"
    route = [Coordinate(0, 0, 0), Coordinate(1, 1, 1), Coordinate(2, 2, 2)]

    uav = UAV(uav_type=uav_type, route=route)

    assert uav.type == uav_type
    assert uav.route == route
