from measurements.cube import Cube


class Measurement:

    def __init__(self, cubes: list[Cube], t: int):
        self.cubes = cubes
        self.t = t
