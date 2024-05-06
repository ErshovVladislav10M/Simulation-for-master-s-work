from sensors.cube import Cube


class Measurement:

    def __init__(self, cubes: list[(Cube, float)], t: int):
        self.cubes = cubes
        self.t = t

    def __str__(self):
        string = "cubes = [\n"
        for cube, q in self.cubes:
            string += str(cube) + ", q = " + str(q) + "\n"
        string += "],\nt = " + str(self.t)

        return string
