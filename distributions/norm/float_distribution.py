from numpy import ndarray
from scipy.stats import norm

from distributions.abstract_distribution import AbstractDistribution


class NormFloatDistribution(AbstractDistribution):

    def __init__(self, peek: float, scale: float):
        self._peek = peek
        self._scale = scale

    def get_values(self, num_of_values: int) -> ndarray[float]:
        return norm.rvs(loc=self._peek, scale=self._scale, size=num_of_values)
