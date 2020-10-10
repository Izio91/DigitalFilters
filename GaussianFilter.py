from DigitalFilter import Filter
import numpy as np

class Gaussian(Filter):
    __standard_deviation = 0
    __kernel = None

    def make_convolution(self, image, output):
        self.make_kernel()
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
                output[i, j] = convolution
        return output

    def make_kernel(self):
        self.set_standard_deviation()
        samples = abs(np.random.normal(0.0, self.__standard_deviation, (self.get_height() * self.get_width())))
        samples = self.normalize_samples(samples)
        self.__kernel = self.fill_kernel(samples)

    def set_standard_deviation(self):
        self.__standard_deviation = (self.get_width() + 1) / 5

    def normalize_samples(self, samples):
        min_sample = min(samples)
        max_sample = max(samples)
        result = samples / (max_sample * min_sample)
        return sorted(result.astype(int), reverse=True)

    def fill_kernel(self, samples):
        x_coordinate_of_middle_kernel = int(self.get_height() / 2)
        if int(self.get_height()) % 2 == 0:
            x_coordinate_of_middle_kernel = x_coordinate_of_middle_kernel - 1
        y_coordinate_of_middle_kernel = int(self.get_width() / 2)
        if int(self.get_width()) % 2 == 0:
            y_coordinate_of_middle_kernel = y_coordinate_of_middle_kernel - 1
        left_index = (self.get_width() * x_coordinate_of_middle_kernel) + x_coordinate_of_middle_kernel
        right_index = left_index
        tmp_list = np.ones(len(samples))
        index = 0
        while index < len(samples):
            if (left_index >= 0 and right_index < len(samples)):
                if (left_index == right_index):
                    if (samples[index] != 0):
                        tmp_list[left_index] = samples[index]
                    index = index + 1
                else:
                    if (samples[index] != 0):
                        tmp_list[left_index] = samples[index]
                    index = index + 1
                    if (samples[index] != 0):
                        tmp_list[right_index] = samples[index]
                    index = index + 1
                left_index = left_index - 1
                right_index = right_index + 1
            else:
                if (left_index >= 0):
                    if (samples[index] != 0):
                        tmp_list[left_index] = samples[index]
                    left_index = left_index - 1
                else:
                    if (samples[index] != 0):
                        tmp_list[right_index] = samples[index]
                    right_index = right_index + 1
                index = index + 1
        return np.reshape(tmp_list.astype(int), (self.get_height(), self.get_width()))