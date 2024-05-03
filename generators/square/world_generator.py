from generators.abstract_generator import AbstractGenerator
from generators.square.build_generator import SquareBuildGenerator
from worlds.coodrinate import Coordinate
from worlds.square.world import SquareWorld


class SquareWorldGenerator(AbstractGenerator):

    def __init__(
        self,
        num_steps: int,
        create_step_images: bool,
        world_vertices: list[Coordinate],
        cube_side_size: float,
        build_generator: SquareBuildGenerator
    ):
        self._num_steps = num_steps
        self._create_step_images = create_step_images
        self._world_vertices = world_vertices
        self._cube_side_size = cube_side_size
        self._build_generator = build_generator

    def create(self) -> SquareWorld:
        world = SquareWorld(
            self._num_steps,
            self._create_step_images,
            self._world_vertices,
            self._cube_side_size
        )

        for build in self._build_generator.create():
            world.builds.append(build)

        return world
