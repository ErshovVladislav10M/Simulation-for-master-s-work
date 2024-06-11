import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from src.measurements.measurement import Measurement
from src.worlds.abstract_drawer import AbstractDrawer
from src.worlds.abstract_world_object import AbstractWorldObject


class CityDrawer(AbstractDrawer):

    def __init__(self, world, path_to_results: str = "results"):
        self._world = world
        self._buildings = world.buildings
        self._sensors = world.cameras
        self._uavs = world.uavs
        self._exclude_areas = world.exclude_areas

        self._path_to_results = path_to_results

    def draw(self, step: int):
        figure = plt.figure(figsize=(5, 5))
        # figure = plt.figure(figsize=(8, 8))

        # sub_plot = figure.add_subplot(1, 2, 1)
        # figure.subplots_adjust(left=0.05, bottom=0.05, top=0.95, right=0.95)
        figure.subplots_adjust(left=0.01, bottom=0.005, top=0.99, right=0.99)
        sub_plot = figure.add_subplot()

        # self._draw_objects(sub_plot, self._exclude_areas, "Excluded area")
        self._draw_objects(sub_plot, self._exclude_areas, "Исключенная область")
        # self._draw_objects(sub_plot, self._buildings, "Buildings")
        self._draw_objects(sub_plot, self._buildings, "Строения")
        self._draw_sensors(sub_plot)
        # self._draw_objects(sub_plot, self._uavs, "UAVs")
        self._draw_objects(sub_plot, self._uavs, "БПЛА")

        # plt.xlabel("Step number: " + str(step), fontsize="xx-large")
        # plt.xlabel("Шаг: " + str(step), fontsize="xx-large")

        sub_plot.set(
            xlim=(-self._world.size, self._world.size),
            ylim=(-self._world.size, self._world.size),
        )

        plt.xticks([])
        plt.yticks([])

        plt.legend(loc="upper right", ncol=1, fontsize="large")

        plt.savefig(
            self._path_to_results + f"/img/img_{step}.png",
            transparent=False,
            facecolor="white",
            dpi=300
        )
        plt.close()

    def _draw_measurements(self, sub_plot: Axes, measurements: list[Measurement]) -> None:
        for measurement in measurements:
            if self._world.actual_step - measurement.t > 0:
                continue

            for cube in measurement.cubes:
                # if cube.q < 0.5:
                #     continue

                patch = cube.create_xy_patch()
                # patch.set_alpha(1 - 0.33 * (self._world.actual_step - measurement.t))
                sub_plot.add_patch(patch)

    def _draw_sensors(self, sub_plot: Axes) -> None:
        for camera in self._sensors:
            self._draw_measurements(sub_plot, camera.get_all_measurements())

        patches = [camera.create_xy_patch() for camera in self._sensors]
        if len(patches) == 0:
            return

        patches[0].set_label("Камеры")

        for patch in patches:
            sub_plot.add_patch(patch)

    @staticmethod
    def _draw_objects(
        sub_plot: Axes,
        world_objects: list[AbstractWorldObject],
        label: str
    ) -> None:
        patches = [world_object.create_xy_patch() for world_object in world_objects]
        if len(patches) == 0 or patches[0] is None:
            return

        patches[0].set_label(label)

        for patch in patches:
            sub_plot.add_patch(patch)
