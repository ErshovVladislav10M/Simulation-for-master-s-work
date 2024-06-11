import json

from src.distributions.uniform.float_distribution import UniformFloatDistribution
from src.generators.city.camera_generator import CameraGenerator


def test():
    with open("test/generators/data/world_config.json", "r", encoding="utf-8") as file:
        simulation_data = json.load(file)

    with open(simulation_data["sensor"], "r", encoding="utf-8") as file:
        sensor_data = json.load(file)
    with open(simulation_data["uav"], "r", encoding="utf-8") as file:
        uav_data = json.load(file)

    uav_type = uav_data["type"]
    detection_distances = sensor_data["detection_distances"]
    detection_distance = detection_distances[uav_type]
    detection_distance_distribution = UniformFloatDistribution(
        min_value=detection_distance,
        max_value=detection_distance
    )

    generator = CameraGenerator(
        simulation_data=simulation_data,
        detection_distance_distribution=detection_distance_distribution,
        sensor_data=sensor_data,
        cube_side=10
    )

    cameras = generator.create(100)
    assert len(cameras) == 100
