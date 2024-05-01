class UAV:

    def __init__(self, route: list[(int, int, int)]):
        self.route = route
        self.step = 0

    def do_step(self) -> None:
        if not self.is_finished():
            self.step += 1

    def is_finished(self) -> bool:
        return len(self.route) > self.step

    def get_coord(self) -> (int, int, int) | None:
        if not self.is_finished():
            return self.route[self.step]
        else:
            return None
