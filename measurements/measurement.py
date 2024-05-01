from measurements.cube import Cube


class Measurement:

    def __init__(self, cubes: list[(Cube, float)], t: int):
        self.cubes = cubes
        self.t = t
