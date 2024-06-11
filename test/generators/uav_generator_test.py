import json

from src.generators.uav_generator import UAVGenerator


def test():
    with open("test/generators/data/world_config.json", "r", encoding="utf-8") as file:
        simulation_data = json.load(file)

    with open(simulation_data["uav"], "r", encoding="utf-8") as file:
        uav_data = json.load(file)

    generator = UAVGenerator(
        simulation_data=simulation_data,
        uav_data=uav_data,
        keep_start_vector=True
    )

    uavs = generator.create(100)
    assert len(uavs) == 100
