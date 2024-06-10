import json

import pytest

from src.distributions.distribution_utils import get_distribution


def test_float_norm():
    with open("./data/float_norm.json", "r") as file:
        distribution_data = json.load(file)

    distribution = get_distribution(distribution_data=distribution_data["distribution"])
    values = distribution.get_values(num_of_values=distribution_data["num_of_values"])

    assert len(values) == 1000
    assert sum(values) / len(values) // 10 < 1


def test_float_uniform():
    with open("./data/float_uniform.json", "r") as file:
        distribution_data = json.load(file)

    distribution = get_distribution(distribution_data=distribution_data["distribution"])
    values = distribution.get_values(num_of_values=distribution_data["num_of_values"])

    assert len(values) == 1000
    assert min(values) >= 10
    assert max(values) <= 100


def test_float_error():
    with open("./data/float_error.json", "r") as file:
        distribution_data = json.load(file)

    with pytest.raises(ValueError):
        get_distribution(distribution_data=distribution_data["distribution"])


def test_coordinate_uniform():
    with open("./data/coordinate_uniform.json", "r") as file:
        distribution_data = json.load(file)

    distribution = get_distribution(distribution_data=distribution_data["distribution"])
    values = distribution.get_values(num_of_values=distribution_data["num_of_values"])

    x_values = [vector.x for vector in values]
    y_values = [vector.y for vector in values]
    z_values = [vector.z for vector in values]

    assert len(values) == 1000

    assert min(x_values) >= 10
    assert min(y_values) >= 10
    assert min(z_values) >= 10

    assert max(x_values) <= 100
    assert max(y_values) <= 100
    assert max(z_values) <= 100


def test_coordinate_error():
    with open("./data/coordinate_error.json", "r") as file:
        distribution_data = json.load(file)

    with pytest.raises(ValueError):
        get_distribution(distribution_data=distribution_data["distribution"])


def test_vector_uniform():
    with open("./data/vector_uniform.json", "r") as file:
        distribution_data = json.load(file)

    distribution = get_distribution(distribution_data=distribution_data["distribution"])
    values = distribution.get_values(num_of_values=distribution_data["num_of_values"])

    x_values = [vector.x for vector in values]
    y_values = [vector.y for vector in values]
    z_values = [vector.z for vector in values]

    assert len(values) == 1000

    assert min(x_values) >= 10
    assert min(y_values) >= 10
    assert min(z_values) >= 10

    assert max(x_values) <= 100
    assert max(y_values) <= 100
    assert max(z_values) <= 100


def test_vector_error():
    with open("./data/vector_error.json", "r") as file:
        distribution_data = json.load(file)

    with pytest.raises(ValueError):
        get_distribution(distribution_data=distribution_data["distribution"])


def test_error():
    with open("./data/error.json", "r") as file:
        distribution_data = json.load(file)

    with pytest.raises(ValueError):
        get_distribution(distribution_data=distribution_data["distribution"])
