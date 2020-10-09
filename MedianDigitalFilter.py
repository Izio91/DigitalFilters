from DigitalFilter import Filter
from MedianFilter import Median

class MedianDigitalFilter(Filter):
    def make_digital_filter(self, height, width):
        return Median(height, width)