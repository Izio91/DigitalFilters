from DigitalFilter import Filter
import numpy as np

class LocalNoise(Filter):
    __kernel = None
    __local_mean_matrix = None
    __local_variance_matrix = None

    def make_convolution(self, image, output):
        self.create_kernel()
        self.fill_local_mean_matrix(image, output)
        self.fill_local_variance_matrix(image, output)
        noise_variance = np.average(self.__local_variance_matrix)

        for i in range(self.__local_variance_matrix.shape[0]):
            for j in range(self.__local_variance_matrix.shape[1]):
                if noise_variance > self.__local_variance_matrix[i, j]:
                    self.__local_variance_matrix[i, j] = noise_variance

        output = image - (noise_variance / self.__local_variance_matrix) * (image - self.__local_mean_matrix)
        return output

    def create_kernel(self):
        self.__kernel = np.zeros((self.get_height(), self.get_width()))

    def fill_local_mean_matrix(self, image, output):
        self.__local_mean_matrix = np.zeros(output.shape)
        self.__local_mean_matrix = self.__local_mean_matrix + output
        starting_row = int(self.get_height() / 2)
        starting_column = int(self.get_width() / 2)
        ending_row = image[:, 0].size - self.get_down_side_frame()
        ending_column = image[0, :].size - self.get_right_side_frame()
        for i in range(starting_row, ending_row):
            for j in range(starting_column, ending_column):
                for q in range(i - self.get_up_side_frame(), i - self.get_up_side_frame() + self.get_height()):
                    for r in range(j - self.get_left_side_frame(), j - self.get_left_side_frame() + self.get_width()):
                        row_kernel = q - i + self.get_up_side_frame()
                        column_kernel = r - j + self.get_left_side_frame()
                        self.__kernel[row_kernel, column_kernel] = image[q, r]
                self.__local_mean_matrix[i, j] = np.average(self.__kernel)
        return self.__local_mean_matrix

    def fill_local_variance_matrix(self, image, output):
        self.__local_variance_matrix = np.zeros(output.shape)
        self.__local_variance_matrix = self.__local_variance_matrix + output
        starting_row = int(self.get_height() / 2)
        starting_column = int(self.get_width() / 2)
        ending_row = image[:, 0].size - self.get_down_side_frame()
        ending_column = image[0, :].size - self.get_right_side_frame()
        for i in range(starting_row, ending_row):
            for j in range(starting_column, ending_column):
                for q in range(i - self.get_up_side_frame(), i - self.get_up_side_frame() + self.get_height()):
                    for r in range(j - self.get_left_side_frame(), j - self.get_left_side_frame() + self.get_width()):
                        row_kernel = q - i + self.get_up_side_frame()
                        column_kernel = r - j + self.get_left_side_frame()
                        self.__kernel[row_kernel, column_kernel] = image[q, r]
                self.__local_variance_matrix[i, j] = np.std(self.__kernel)
        return self.__local_variance_matrix

