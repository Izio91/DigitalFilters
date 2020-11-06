from DigitalFilter import Filter
from GaussianFilter import Gaussian
import numpy as np
from Utilities import show_image
class Unsharpening(Filter):
    __gaussian_filter = None

    def __init__(self, size=3):
        self.__gaussian_filter = Gaussian(size)

    def make_convolution(self, image, output):
        output = image + (image - self.__gaussian_filter.apply_to_image(image))
        output = self.delete_outliers(output)
        return output.astype(np.uint8)

    def image_is_in_gray_scale(self, image):
        return len(image.shape) == 2

    def delete_outliers(self, output):
        for i in range(output.shape[0]):
            for j in range(output.shape[1]):
                if not self.image_is_in_gray_scale(output):
                    if output[i][j][0] < 0:
                        output[i][j][0] = 0
                    elif output[i][j][0] > 254:
                        output[i][j][0] = 254

                    if output[i][j][1] < 0:
                        output[i][j][1] = 0
                    elif output[i][j][1] > 254:
                        output[i][j][1] = 254

                    if output[i][j][2] < 0:
                        output[i][j][2] = 0
                    elif output[i][j][2] > 254:
                        output[i][j][2] = 254
                else:
                    if output[i][j] < 0:
                        output[i][j] = 0
                    elif output[i][j] > 254:
                        output[i][j] = 254
        return output