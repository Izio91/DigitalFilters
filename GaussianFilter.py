from DigitalFilter import Filter
import numpy as np
import scipy.stats as st

class Gaussian(Filter):
    __standard_deviation = 0
    __kernel = None

    def __init__(self, size=3):
        self.set_height(size)
        self.set_width(size)
        self.make_kernel()

    def make_convolution(self, image, output):
        starting_row = int(self.get_height() / 2)
        starting_column = int(self.get_width() / 2)
        ending_row = image[:, 0].size - self.get_down_side_frame()
        ending_column = image[0, :].size - self.get_right_side_frame()
        for i in range(starting_row, ending_row):
            for j in range(starting_column, ending_column):
                convolution = 0
                for q in range(i - self.get_up_side_frame(), i - self.get_up_side_frame() + self.get_height()):
                    for r in range(j - self.get_left_side_frame(), j - self.get_left_side_frame() + self.get_width()):
                        row_kernel = q - i + self.get_up_side_frame()
                        column_kernel = r - j + self.get_left_side_frame()
                        convolution = convolution + (self.__kernel[row_kernel, column_kernel] * image[q, r])
                output[i, j] = int(convolution)
        return output

    def make_kernel(self):
        """Returns a 2D Gaussian kernel."""
        self.set_standard_deviation()
        x = np.linspace(-self.__standard_deviation, self.__standard_deviation, self.get_height() + 1)
        kern1d = np.diff(st.norm.cdf(x))
        kern2d = np.outer(kern1d, kern1d)
        self.__kernel = kern2d / kern2d.sum()
        self.__kernel = self.__kernel / self.__kernel[0, 0]
        self.__kernel = self.__kernel / self.__kernel.sum()

    def set_standard_deviation(self):
        self.__standard_deviation = (self.get_width() + 1) / 5

