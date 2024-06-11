import json

import pytest

from src.distributions.distribution_utils import get_distribution
from src.distributions.norm.float_distribution import NormFloatDistribution
from src.distributions.uniform.coordinate_distribution import UniformCoordinateDistribution
from src.distributions.uniform.float_distribution import UniformFloatDistribution
from src.distributions.uniform.vector_distribution import UniformVectorDistribution


def test_float_norm():
    with open("test/distributions/data/float_norm.json", "r") as file:
        distribution_data = json.load(file)

    distribution = get_distribution(distribution_data=distribution_data["distribution"])

    assert isinstance(distribution, NormFloatDistribution)


def test_float_uniform():
    with open("test/distributions/data/float_uniform.json", "r") as file:
        distribution_data = json.load(file)

    distribution = get_distribution(distribution_data=distribution_data["distribution"])

    assert isinstance(distribution, UniformFloatDistribution)


def test_float_error():
    with open("test/distributions/data/float_error.json", "r") as file:
        distribution_data = json.load(file)

    with pytest.raises(ValueError):
        get_distribution(distribution_data=distribution_data["distribution"])


def test_coordinate_uniform():
    with open("test/distributions/data/coordinate_uniform.json", "r") as file:
        distribution_data = json.load(file)

    distribution = get_distribution(distribution_data=distribution_data["distribution"])

    assert isinstance(distribution, UniformCoordinateDistribution)


def test_coordinate_error():
    with open("test/distributions/data/coordinate_error.json", "r") as file:
        distribution_data = json.load(file)

    with pytest.raises(ValueError):
        get_distribution(distribution_data=distribution_data["distribution"])


def test_vector_uniform():
    with open("test/distributions/data/vector_uniform.json", "r") as file:
        distribution_data = json.load(file)

    distribution = get_distribution(distribution_data=distribution_data["distribution"])

    assert isinstance(distribution, UniformVectorDistribution)


def test_vector_error():
    with open("test/distributions/data/vector_error.json", "r") as file:
        distribution_data = json.load(file)

    with pytest.raises(ValueError):
        get_distribution(distribution_data=distribution_data["distribution"])


def test_error():
    with open("test/distributions/data/error.json", "r") as file:
        distribution_data = json.load(file)

    with pytest.raises(ValueError):
        get_distribution(distribution_data=distribution_data["distribution"])
