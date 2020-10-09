from DigitalFilter import Filter
from AverageFilter import Average

class AverageDigitalFilter(Filter):
    def make_digital_filter(self, height, width):
        return Average(height, width)
