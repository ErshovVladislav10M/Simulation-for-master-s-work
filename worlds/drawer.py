import math

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import RegularPolygon, Circle, Arrow

from sensors.camera import Camera
from uavs.uav import UAV
from worlds.area import Area


class Drawer2D:

    def __init__(
        self,
        cameras: list[Camera],
        uavs: list[UAV],
        path_to_results: str = "results",
        create_step_images: bool = True
    ):
        self._cameras = cameras
        self._uavs = uavs

        self._path_to_results = path_to_results
        self._create_step_images = create_step_images

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

        self._draw_cameras(sub_plot)
        self._draw_uavs(sub_plot)

        plt.xlabel("Step number: " + str(step), fontsize="xx-large")
        sub_plot.set(
            xlim=(-10, 10),
            ylim=(-10, 10),
        )

        plt.xticks([])
        plt.yticks([])
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

    def _draw_area(self, sub_plot: Axes, area: Area, id: int) -> None:
        for cube in area.cubes:
            polygon = RegularPolygon(
                xy=(cube.x, cube.y),
                numVertices=4,
                radius=math.sqrt(2) / 2,
                orientation=0.25 * math.pi,
                edgecolor=self._colors[id],
                linewidth=0,
                facecolor="white",
                hatch="..",
            )

            sub_plot.add_patch(polygon)

    def _draw_cameras(self, sub_plot: Axes) -> None:
        for camera in self._cameras:
            self._draw_area(sub_plot, camera._area, camera.id)

            position = camera.position
            circle = Circle(
                xy=(position.x, position.y),
                radius=0.2,
                edgecolor=self._colors[camera.id],
            )
            circle.set_label("Camera " + str(camera.id))
            sub_plot.add_patch(circle)

    def _draw_uavs(self, sup_plot: Axes):
        for uav in self._uavs:
            position = uav.get_position()
            next_position = uav.get_next_position()
            if position is None or next_position is None:
                continue

            arrow = Arrow(
                x=position.x,
                y=position.y,
                dx=next_position.x - position.x,
                dy=next_position.y - position.y,
                width=1,
                facecolor="red",
            )

            sup_plot.add_patch(arrow)

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
