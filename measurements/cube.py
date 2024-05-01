class Cube:

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if not isinstance(other, Cube):
            return False

        return self.x == other.x\
            and self.y == other.y\
            and self.z == other.z
