import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np
import re


def get_percents(sim_name: str, cube_side: int):
    with open("results/" + sim_name + "/actual_uavs_" + str(cube_side) + ".txt", "r") as file:
        actual_uavs_counts = [int(count) for count in list(re.split("[\[,\]]", file.readline())) if count != ""]

    with open("results/" + sim_name + "/detected_uavs_" + str(cube_side) + ".txt", "r") as file:
        detected_uavs_counts = [int(count) for count in list(re.split("[\[,\]]", file.readline())) if count != ""]

    return [
        100 * float(detected_uavs_count) / actual_uavs_count
        for actual_uavs_count, detected_uavs_count in zip(actual_uavs_counts, detected_uavs_counts)
    ]


def draw():
    sim_name = "geran2_h10"
    # percents_cube_side_5 = get_percents(5)
    percents_cube_side_10 = get_percents(sim_name, 10)
    percents_cube_side_15 = get_percents(sim_name, 15)

    figure = plt.figure(figsize=(5, 5))

    plt.xlabel("Шаги")
    plt.ylabel("Процент обнаруженных БПЛА")
    plt.xlim(-2, len(percents_cube_side_15) + 2)
    plt.ylim(-2, 102)
    plt.title("Эффективность обнаружения БПЛА")

    # time_steps_smooth = np.linspace(0, 69, 200)
    # spl = make_interp_spline([i for i in range(0, 70)], diameter1, k=5)
    # diameter1_smooth = spl(time_steps_smooth)
    # spl = make_interp_spline([i for i in range(0, 70)], diameter2, k=5)
    # diameter2_smooth = spl(time_steps_smooth)
    # spl = make_interp_spline([i for i in range(0, 70)], diameter3, k=5)
    # diameter3_smooth = spl(time_steps_smooth)

    # plt.plot([i for i in range(len(percents_cube_side_5))], percents_cube_side_5, "r-", label="Сторона куба 5")
    plt.plot([i for i in range(len(percents_cube_side_10))], percents_cube_side_10, "g-", label="Сторона куба 10")
    plt.plot([i for i in range(len(percents_cube_side_15))], percents_cube_side_15, "b-", label="Сторона куба 15")
    plt.legend(loc="upper right")

    # sub_plot = figure.add_subplot(1, 2, 2)
    # plt.xlabel("Time steps")
    # plt.ylabel("Accuracy")
    # plt.xlim(-2, 72)
    # plt.ylim(-2, max(accuracy1) + 5)
    # # plt.title("Accuracy for 10 agents on 24*24 plane")
    #
    # time_steps_smooth = np.linspace(0, 69, 200)
    # spl = make_interp_spline([i for i in range(0, 70)], accuracy1, k=5)
    # accuracy1_smooth = spl(time_steps_smooth)
    # spl = make_interp_spline([i for i in range(0, 70)], accuracy2, k=5)
    # accuracy2_smooth = spl(time_steps_smooth)
    # spl = make_interp_spline([i for i in range(0, 70)], accuracy3, k=5)
    # accuracy3_smooth = spl(time_steps_smooth)
    #
    # sub_plot.plot([i for i in range(0, 70)], accuracy1, "r-", label="Micro-control")
    # sub_plot.plot([i for i in range(0, 70)], accuracy2, "g-", label="Macro-control")
    # sub_plot.plot([i for i in range(0, 70)], accuracy3, "b-", label="Meso-control")
    # sub_plot.legend(loc="best")

    # plt.show()
    plt.savefig("./results/" + sim_name + "/grade.png", transparent=False, facecolor="white", dpi=170)


if __name__ == "__main__":
    # figure = plt.figure(figsize=(15, 5))
    #
    # sub_plot = figure.add_subplot(1, 3, 1)
    # draw(5, sub_plot)
    # sub_plot = figure.add_subplot(1, 3, 2)
    # draw(10, sub_plot)
    # sub_plot = figure.add_subplot(1, 3, 3)
    # draw(15, sub_plot)

    draw()
