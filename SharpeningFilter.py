import numpy as np
from DigitalFilter import Filter

class Sharpening(Filter):
    __kernel = None

    def __init__(self):
        size = 3
        self.set_height(size)
        self.set_width(size)
        self.make_kernel()

    def make_kernel(self):
        self.__kernel = np.ones((self.get_height(), self.get_width()))
        row_of_middle_pixel_inside_kernel = int(self.get_height() / 2)
        column_of_middle_pixel_inside_kernel = int(self.get_width() / 2)

        self.__kernel[row_of_middle_pixel_inside_kernel, column_of_middle_pixel_inside_kernel] = -8

    def make_convolution(self, image, output):
        laplacian_mask = self.apply_derivative(image)
        output = image - laplacian_mask
        return output

    def apply_derivative(self, image):
        laplacian_mask = np.zeros(image.shape)
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
                laplacian_mask[i, j] = int(convolution)
        return laplacian_mask