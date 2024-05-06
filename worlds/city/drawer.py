import math

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import RegularPolygon

from sensors.cameras.camera import Camera
from sensors.cube_area import CubeArea
from uavs.uav import UAV
from worlds.abstract_world_object import AbstractWorldObject
from worlds.area import Area
from worlds.city.building import CityBuilding


class CityDrawer:

    def __init__(
        self,
        buildings: list[CityBuilding],
        cameras: list[Camera],
        uavs: list[UAV],
        exclude_areas: list[Area],
        cube_side_size: float,
        path_to_results: str = "results"
    ):
        self._buildings = buildings
        self._cameras = cameras
        self._uavs = uavs
        self._exclude_areas = exclude_areas
        self._cube_side_size = cube_side_size

        self._path_to_results = path_to_results

        self._colors = [
            "gray",
            "blue",
            "red",
            "purple",
            "green",
            "deeppink",
            "brown",
            "cyan",
            "antiquewhite",
            "darkgreen",
            "darkviolet",
            "goldenrod",
            "lawngreen",
            "mediumaquamarine",
            "navy",
            "sienna",
            "greenyellow",
            "hotpink",
            "ivory",
            "moccasin",
            "coral",
            "darkgoldenrod",
            "mediumseagreen",
            "lightyellow",
            "mintcream",
            "linen",
            "chocolate",
            "aliceblue",
            "darkred",
            "tomato",
            "royalblue",
        ]

    def draw_plane(self, num_steps: int, step: int):
        figure = plt.figure(figsize=(8, 8))
        # figure = plt.figure(figsize=(6, 6))

        # sub_plot = figure.add_subplot(1, 2, 1)
        sub_plot = figure.add_subplot()

        self._draw_objects(sub_plot, self._exclude_areas, "Exclude area")
        self._draw_objects(sub_plot, self._buildings, "Buildings")
        self._draw_cameras(sub_plot)
        self._draw_objects(sub_plot, self._uavs, "UAVs")

        plt.xlabel("Step number: " + str(step), fontsize="xx-large")
        sub_plot.set(
            xlim=(-200, 200),
            ylim=(-200, 200),
        )

        # plt.xticks([])
        # plt.yticks([])
        plt.legend(loc="upper right", ncol=2, fontsize="x-large")

        # plt.subplot(1, 2, 2)
        # plt.xlabel("Time steps")
        # plt.ylabel("Conventional units")
        # plt.xlim(-4, 134)
        # plt.ylim(-2, self.num_of_titles_side * len(agents))
        # plt.plot(self.steps, self.accuracy, "r-", label="Accuracy")
        # plt.plot(self.steps, self.max_diameter, "b-", label="Diameter")
        #
        # plt.legend(loc="best")

        # if step == num_steps - 1:
        #     f = open(self._path_to_results + "/accuracy.txt", "w")
        #     f.write(str(self.accuracy))
        #     f.close()
        #     f = open(self._path_to_results + "/diameter.txt", "w")
        #     f.write(str(self.diameter))
        #     f.close()

        plt.savefig(
            self._path_to_results + f"/img/img_{step}.png",
            transparent=False,
            facecolor="white",
            dpi=300
        )
        plt.close()

    def _draw_cube_area(self, sub_plot: Axes, area: CubeArea) -> None:
        for cube in area.cubes:
            polygon = RegularPolygon(
                xy=(cube.coordinate.x, cube.coordinate.y),
                numVertices=4,
                radius=math.sqrt(2 * cube.side * cube.side) / 2,
                orientation=0.25 * math.pi,
                edgecolor="blue",
                linewidth=0,
                facecolor="white",
                hatch="xx",
            )
            sub_plot.add_patch(polygon)

    def _draw_cameras(self, sub_plot: Axes) -> None:
        # for camera in self._cameras:
        #     self._draw_cube_area(sub_plot, camera._area)

        patches = [camera.create_patch() for camera in self._cameras]
        if len(patches) == 0:
            return

        patches[0].set_label("Cameras")

        for patch in patches:
            sub_plot.add_patch(patch)

    @staticmethod
    def _draw_objects(
        sub_plot: Axes,
        world_objects: list[AbstractWorldObject],
        label: str
    ) -> None:
        patches = [world_object.create_patch() for world_object in world_objects]
        if len(patches) == 0 or patches[0] is None:
            return

        patches[0].set_label(label)

        for patch in patches:
            sub_plot.add_patch(patch)

    # def get_accuracy(self) -> int:
    #     sum_accuracy = 0
    #     for agent in self._cameras:
    #         sum_accuracy += agent.behaviour.agent_location.get_distance(agent.behaviour.target_location)
    #     return sum_accuracy
    #
    # def get_diameter(self) -> int:
    #     diameter = 0
    #     for agent_i in self._cameras:
    #         for agent_j in self._cameras:
    #             distance = agent_j.behaviour.agent_location.get_distance(agent_i.behaviour.agent_location)
    #             if distance > diameter:
    #                 diameter = distance
    #
    #     return diameter
