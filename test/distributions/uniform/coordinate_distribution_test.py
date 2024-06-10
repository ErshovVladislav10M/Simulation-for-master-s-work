from src.distributions.uniform.coordinate_distribution import UniformCoordinateDistribution
from src.worlds.coodrinate import Coordinate


def test():
    distribution = UniformCoordinateDistribution(
        min_value=Coordinate(10, 10, 10),
        max_value=Coordinate(100, 100, 100)
    )
    values = distribution.get_values(num_of_values=1000)

    assert len(values) == 1000

    assert min([vector.x for vector in values]) >= 10
    assert min([vector.y for vector in values]) >= 10
    assert min([vector.z for vector in values]) >= 10

    assert max([vector.x for vector in values]) <= 100
    assert max([vector.y for vector in values]) <= 100
    assert max([vector.z for vector in values]) <= 100
