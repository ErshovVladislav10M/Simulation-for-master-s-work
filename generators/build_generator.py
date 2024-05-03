from generators.abstract_generator import AbstractGenerator
from worlds.coodrinate import Coordinate
from worlds.world import World
from skipy.stats import norm


class BuildGenerator(AbstractGenerator):

    def __init__(
        self,
        average_height: int,
        height_distribution: bool,
        world_vertices: list[Coordinate],
        cube_side_size: float
    ):
        self._average_height = average_height
        self._create_step_images = create_step_images
        self._world_vertices = world_vertices
        self._cube_side_size = cube_side_size

    def create(self) -> World:
        return World(
            self._num_steps,
            self._create_step_images,
            self._world_vertices,
            self._cube_side_size
        )
