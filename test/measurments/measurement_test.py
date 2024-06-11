from src.measurements.measurement import Measurement
from src.sensors.cube import Cube
from src.worlds.coodrinate import Coordinate


def test():
    sensor_id = 12
    cubes = [Cube(coordinate=Coordinate(0, 0, 0), side=1, q=0.5)]
    t = 13
    measurement = Measurement(sensor_id=sensor_id, cubes=cubes, t=t)

    assert measurement.sensor_id == sensor_id
    assert measurement.cubes == cubes
    assert measurement.t == t
