import os
import re

import matplotlib.pyplot as plt


def get_percent(uav: str, h: int, cube_side: int) -> float:
    actual_uav_file = "results/" + uav + "_h" + str(h) + "/actual_uavs_" + str(cube_side) + ".txt"
    if not os.path.isfile(actual_uav_file):
        return -1
    with open(actual_uav_file, "r", encoding="utf-8") as file:
        actual_uavs_counts = [int(count) for count in list(re.split(r"[\[,\]]", file.readline())) if count != ""]

    detected_uav_file = "results/" + uav + "_h" + str(h) + "/detected_uavs_" + str(cube_side) + ".txt"
    if not os.path.isfile(detected_uav_file):
        return -1
    with open(detected_uav_file, "r", encoding="utf-8") as file:
        detected_uavs_counts = [int(count) for count in list(re.split(r"[\[,\]]", file.readline())) if count != ""]

    return 100.0 * sum(detected_uavs_counts) / sum(actual_uavs_counts)


def draw(cube_side: int):
    plt.xlabel("Высота полета (м)")
    plt.ylabel("Процент обнаруженных БПЛА")
    plt.xlim(0, 50)
    plt.ylim(-2, 102)
    plt.title("Эффективность обнаружения БПЛА")

    uav_names = {
        "cavok": "Cavok 23 VH",
        "geran2": "Герань-2",
        "matrice600": "DJI Matrice 600 Pro",
        "mavic3": "DJI Mavic 3 Enterprise"
    }
    uav_colors = {"cavok": "k", "geran2": "r", "matrice600": "b", "mavic3": "m"}

    for uav in ["geran2", "cavok", "matrice600", "mavic3"]:
        heights = []
        percents = []
        for h in [5, 10, 15, 20, 25, 30, 35, 40, 45]:
            percent = get_percent(uav, h, cube_side)
            if percent < 0:
                continue

            heights.append(h)
            percents.append(percent)

        plt.plot(heights, percents, uav_colors[uav] + "-", label=uav_names[uav])

    plt.legend(loc="upper right")

    # sub_plot = figure.add_subplot(1, 2, 2)
    # sub_plot.legend(loc="best")

    # plt.show()
    plt.savefig("./results/grade_cube_side" + str(cube_side) + ".jpg", transparent=False, facecolor="white", dpi=170)
    plt.close()


if __name__ == "__main__":
    # figure = plt.figure(figsize=(15, 5))
    #
    # sub_plot = figure.add_subplot(1, 3, 1)
    # draw(5, sub_plot)
    # sub_plot = figure.add_subplot(1, 3, 2)
    # draw(10, sub_plot)
    # sub_plot = figure.add_subplot(1, 3, 3)
    # draw(15, sub_plot)

    for side in [10, 15]:
        draw(side)
