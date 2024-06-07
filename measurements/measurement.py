from sensors.cube import Cube


class Measurement:

    def __init__(self, sensor_id: int, cubes: list[Cube], t: int):
        self.sensor_id = sensor_id
        self.cubes = cubes
        self.t = t

    def compare_and_update(self, other) -> None:
        if not isinstance(other, Measurement) or self.sensor_id == other.sensor_id:
            return

        for self_cube in self.cubes:
            for other_cube in other.cubes:
                if self_cube.contain(other_cube.coordinate):
                    self_cube.q = min(self_cube.q + 0.4, 1.0)
                    other_cube.q = min(other_cube.q + 0.4, 1.0)

    def __eq__(self, other):
        if not isinstance(other, Measurement):
            return False

        return self.sensor_id == other.sensor_id \
            and self.cubes == other.cubes \
            and self.t == other.t

    def __str__(self):
        string = "sensor id = " + str(self.sensor_id) + ",\ncubes = [\n"
        for cube, q in self.cubes:
            string += str(cube) + ", q = " + str(q) + "\n"
        string += "],\nt = " + str(self.t)

        return string
