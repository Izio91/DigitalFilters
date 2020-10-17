import numpy as np
from DigitalFilter import Filter

class Sharpening(Filter):
    __kernel = None

    def __init__(self, size=3):
        self.set_height(size)
        self.set_width(size)
        self.make_kernel()

    def make_kernel(self):
        self.__kernel = np.zeros((self.get_height(), self.get_width()))
        row_of_middle_pixel_inside_kernel = int(self.get_height() / 2)
        column_of_middle_pixel_inside_kernel = int(self.get_width() / 2)

        self.__kernel[row_of_middle_pixel_inside_kernel, column_of_middle_pixel_inside_kernel] = -4
        for i in range(self.get_height()):
            if i != row_of_middle_pixel_inside_kernel:
                self.__kernel[i, column_of_middle_pixel_inside_kernel] = 1
        for j in range(self.get_width()):
            if j != column_of_middle_pixel_inside_kernel:
                self.__kernel[row_of_middle_pixel_inside_kernel, j] = 1

    def make_convolution(self, image, output):
        first_derivative = np.copy(output)
        second_derivative = np.copy(output)
        first_derivative = self.apply_derivative(image, first_derivative)
        second_derivative = self.apply_derivative(first_derivative, second_derivative)
        output = image + first_derivative - second_derivative
        return output

    def apply_derivative(self, image, output):
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