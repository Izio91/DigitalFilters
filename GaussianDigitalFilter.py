from DigitalFilter import Filter
from GaussianFilter import Gaussian

class GaussianDigitalFilter(Filter):
    def make_digital_filter(self, height, width):
        return Gaussian(height, width)