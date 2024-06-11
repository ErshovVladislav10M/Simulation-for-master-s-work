import json

from src.distributions.uniform.float_distribution import UniformFloatDistribution
from src.generators.city.camera_generator import CameraGenerator
from src.generators.city.world_generator import CityWorldGenerator


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

    camera_generator = CameraGenerator(
        simulation_data=simulation_data,
        detection_distance_distribution=detection_distance_distribution,
        sensor_data=sensor_data,
        cube_side=10
    )

    generator = CityWorldGenerator(
        simulation_data=simulation_data,
        exclude_areas=[],
        camera_generator=camera_generator
    )

    worlds = generator.create(1)
    assert len(worlds) == 1

    world = worlds[0]
    assert 0 < len(world.buildings) <= 200
    assert len(world.cameras) == 10
    assert len(world.uavs) == 15
