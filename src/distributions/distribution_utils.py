from src.distributions.abstract_distribution import AbstractDistribution
from src.distributions.norm.float_distribution import NormFloatDistribution
from src.distributions.uniform.coordinate_distribution import UniformCoordinateDistribution
from src.distributions.uniform.float_distribution import UniformFloatDistribution
from src.distributions.uniform.vector_distribution import UniformVectorDistribution
from src.worlds.coodrinate import Coordinate
from src.worlds.vector import Vector


def get_distribution(distribution_data: dict) -> AbstractDistribution:
    data_type = distribution_data["data_type"]
    if data_type == "float":
        return _get_float_distribution(distribution_data)

    if data_type == "coordinate":
        return _get_coordinate_distribution(distribution_data)

    if data_type == "vector":
        return _get_vector_distribution(distribution_data)

    raise ValueError("Unknown data type of distribution")


def _get_float_distribution(distribution_data: dict) -> AbstractDistribution:
    kind = distribution_data["kind"]
    if kind == "norm":
        return NormFloatDistribution(distribution_data["peek"], distribution_data["scale"])

    if kind == "uniform":
        return UniformFloatDistribution(distribution_data["min_value"], distribution_data["max_value"])

    raise ValueError("Unknown kind of distribution")


def _get_coordinate_distribution(distribution_data) -> AbstractDistribution:
    kind = distribution_data["kind"]
    if kind == "uniform":
        return UniformCoordinateDistribution(
            Coordinate.of(distribution_data["min_value"]),
            Coordinate.of(distribution_data["max_value"])
        )

    raise ValueError("Unknown kind of distribution")


def _get_vector_distribution(distribution_data) -> AbstractDistribution:
    kind = distribution_data["kind"]
    if kind == "uniform":
        return UniformVectorDistribution(
            Vector.of(Coordinate.of(distribution_data["min_value"])),
            Vector.of(Coordinate.of(distribution_data["max_value"]))
        )

    raise ValueError("Unknown kind of distribution")
