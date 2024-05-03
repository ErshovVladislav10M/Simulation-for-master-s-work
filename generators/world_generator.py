from generators.abstract_generator import AbstractGenerator
from worlds.coodrinate import Coordinate
from worlds.world import World


class WorldGenerator(AbstractGenerator):

    def __init__(
        self,
        num_steps: int,
        create_step_images: bool,
        world_vertices: list[Coordinate],
        cube_side_size: float
    ):
        self._num_steps = num_steps
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
