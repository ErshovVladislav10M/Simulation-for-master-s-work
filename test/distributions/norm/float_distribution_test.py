from src.distributions.norm.float_distribution import NormFloatDistribution


def test():
    distribution = NormFloatDistribution(peek=10, scale=1)
    values = distribution.get_values(num_of_values=1000)

    assert len(values) == 1000
    assert sum(values) / len(values) // 10 < 1
