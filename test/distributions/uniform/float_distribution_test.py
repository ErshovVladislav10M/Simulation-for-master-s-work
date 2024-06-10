from src.distributions.uniform.float_distribution import UniformFloatDistribution


def test():
    distribution = UniformFloatDistribution(min_value=10, max_value=100)
    values = distribution.get_values(num_of_values=1000)

    assert len(values) == 1000
    assert min(values) >= 10
    assert max(values) <= 100
