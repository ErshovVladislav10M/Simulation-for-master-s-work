import math

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import Arc

from measurements.measurement import Measurement
from sensors.cameras.camera import Camera
from uavs.uav import UAV
from worlds.abstract_world import AbstractWorld
from worlds.abstract_world_object import AbstractWorldObject
from worlds.area import Area
from worlds.city.building import CityBuilding
from worlds.vector import Vector


class CityDrawer:

    def __init__(
        self,
        world: AbstractWorld,
        buildings: list[CityBuilding],
        cameras: list[Camera],
        uavs: list[UAV],
        exclude_areas: list[Area],
        path_to_results: str = "results"
    ):
        self._world = world
        self._buildings = buildings
        self._cameras = cameras
        self._uavs = uavs
        self._exclude_areas = exclude_areas

        self._path_to_results = path_to_results
        self._detected_uavs_counts = []
        self._actual_uavs_counts = []

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

        if self._world._create_step_images:
            # self._draw_objects(sub_plot, self._exclude_areas, "Excluded area")
            self._draw_objects(sub_plot, self._exclude_areas, "Исключенная область")
            # self._draw_objects(sub_plot, self._buildings, "Buildings")
            self._draw_objects(sub_plot, self._buildings, "Строения")
            self._draw_cameras(sub_plot)
            # self._draw_objects(sub_plot, self._uavs, "UAVs")
            self._draw_objects(sub_plot, self._uavs, "БПЛА")

        self._detect(num_steps, step)

        plt.xlabel("Step number: " + str(step), fontsize="xx-large")
        sub_plot.set(
            xlim=(-self._world.size, self._world.size),
            ylim=(-self._world.size, self._world.size),
        )

        plt.xticks([])
        plt.yticks([])

        plt.legend(loc="upper right", ncol=1, fontsize="large")
        # plt.legend(loc="best")

        # plt.subplot(1, 2, 2)
        # plt.xlabel("Time steps")
        # plt.ylabel("Conventional units")
        # plt.xlim(-4, 134)
        # plt.ylim(-2, self.num_of_titles_side * len(agents))
        # plt.plot(self.steps, self.accuracy, "r-", label="Accuracy")
        # plt.plot(self.steps, self.max_diameter, "b-", label="Diameter")

        if self._world._create_step_images:
            plt.savefig(
                self._path_to_results + f"/img/img_{step}.png",
                transparent=False,
                facecolor="white",
                dpi=300
            )
        plt.close()

    def _detect(self, num_steps: int, step: int):
        cubes = []
        for camera in self._cameras:
            for measurement in camera.get_actual_measurements(step):
                for cube in measurement.cubes:
                    if cube.q > 0.7:
                        cubes.append(cube)

        actual_uavs = [
            uav
            for uav in self._uavs
            if -self._world.size < uav.get_coordinate().x < self._world.size
               and -self._world.size < uav.get_coordinate().y < self._world.size
        ]

        count_detected_uav = 0
        for uav in actual_uavs:
            for cube in cubes:
                if cube.contain(uav.get_coordinate(), radius=cube.diagonal):
                    count_detected_uav += 1
                    break

        print("Buildings " + str(len(self._buildings)))
        print("Cameras " + str(len(self._cameras)))
        print("Detected " + str(count_detected_uav) + " of " + str(len(actual_uavs)))

        self._detected_uavs_counts.append(count_detected_uav)
        self._actual_uavs_counts.append(len(actual_uavs))
        if step == num_steps - 1:
            f = open(self._path_to_results + "/detected_uavs_" + str(self._cameras[0]._cube_side) + ".txt", "w")
            f.write(str(self._detected_uavs_counts))
            f.close()
            f = open(self._path_to_results + "/actual_uavs_" + str(self._cameras[0]._cube_side) + ".txt", "w")
            f.write(str(self._actual_uavs_counts))
            f.close()

    def _draw_measurements(self, sub_plot: Axes, measurements: list[Measurement]) -> None:
        for measurement in measurements:
            if self._world.actual_step - measurement.t > 0:
                continue

            for cube in measurement.cubes:
                # if cube.q < 0.5:
                #     continue

                patch = cube.create_xy_patch()
                # patch.set_alpha(1 - 0.2 * (self._world.actual_step - measurement.t))
                sub_plot.add_patch(patch)

    def _draw_cameras(self, sub_plot: Axes) -> None:
        for camera in self._cameras:
            self._draw_measurements(sub_plot, camera.get_all_measurements())

        # patches = [camera.create_xy_patch() for camera in self._cameras]
        # if len(patches) == 0:
        #     return
        #
        # patches[0].set_label("Камеры")

        # for patch, camera in zip(patches, self._cameras):
        #     coord = camera._alpha_coordinates[1]
        #     left = camera._alpha_coordinates[0]
        #     right = camera._alpha_coordinates[2]
        #     theta1 = Vector.of(right - coord).get_angle(Vector(0, 1, 0)) / math.pi * 180
        #     theta2 = Vector.of(left - coord).get_angle(Vector(0, 1, 0)) / math.pi * 180
        #     if coord.x > right.x:
        #         theta1 = 180 - theta1
        #     if coord.x > left.x:
        #         theta2 = 180 - theta2
        #     arc = Arc(
        #         xy=(coord.x, coord.y),
        #         width=2 * camera._distance,
        #         height=2 * camera._distance,
        #         theta1=theta1,
        #         theta2=theta2,
        #         # theta1=270,
        #         # theta2=90 + 360,
        #         edgecolor="blue",
        #         alpha=0.2
        #     )
        #     sub_plot.add_patch(arc)
        #     sub_plot.add_patch(patch)

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
