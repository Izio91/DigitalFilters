import numpy as np
from DigitalFilter import Filter
from GaussianFilter import Gaussian

class Unsharpening(Filter):
    __gaussian_filter = None

    def __init__(self, size=3):
        self.__gaussian_filter = Gaussian(size)

    def make_convolution(self, image, output):
        output = image + (image - self.__gaussian_filter.apply_to_image(image))
        return output