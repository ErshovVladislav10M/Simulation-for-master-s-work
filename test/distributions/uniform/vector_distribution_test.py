from src.distributions.uniform.vector_distribution import UniformVectorDistribution
from src.worlds.coodrinate import Coordinate
from src.worlds.vector import Vector


def test():
    distribution = UniformVectorDistribution(
        min_value=Vector.of(Coordinate(10, 10, 10)),
        max_value=Vector.of(Coordinate(100, 100, 100))
    )
    values = distribution.get_values(num_of_values=1000)
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
