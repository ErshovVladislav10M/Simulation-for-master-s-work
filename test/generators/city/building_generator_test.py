import json

from src.distributions.distribution_utils import get_distribution
from src.generators.city.building_generator import CityBuildingGenerator


def test():
    with open("test/generators/data/building_config.json", "r", encoding="utf-8") as file:
        building_data = json.load(file)

    generator = CityBuildingGenerator(
        coordinate_distribution=get_distribution(building_data["coordinate_distribution"]),
        height_distribution=get_distribution(building_data["height_distribution"]),
        side_distribution=get_distribution(building_data["side_distribution"])
    )

    buildings = generator.create(100)
    assert len(buildings) == 100
